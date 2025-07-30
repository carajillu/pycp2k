import os, sys, subprocess

from ase.io import write

from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.xTB_templates import add_xTB_OT
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from pycp2k.templates.PRINT.singlepoint import *
from pycp2k.workflows.mk_mace_dataset import load_dataset,get_elements,add_isolated_atoms

from dask_jobqueue import SLURMCluster
from dask.distributed import Client, wait

def parse():
    """Parse command line arguments."""
    import argparse
    parser = argparse.ArgumentParser(description="Run CP2K calculations in parallel using Dask.")
    parser.add_argument("--cp2k_command", type=str, default="cp2k.psmp")
    parser.add_argument("--dataset", type=str, default="mace_dataset")
    parser.add_argument("--method", type=str, default="xtb", choices=["xtb", "pbe"], help="Method to use for calculations (xtb or pbe).")
    parser.add_argument("--slurm_config", type=str, default="slurm.sh", help="SLURM configuration file to use when creating dask cluster.")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()

def parse_slurm_config(config_file):
    """
    Parse a SLURM job script and extract:
    - SLURM parameters as key-value pairs (e.g. "--mem": "8G")
    - Job script prologue lines (non-comment shell commands)
    """
    config = {"slurm": {}, "prologue": []}

    with open(config_file, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("#SBATCH"):
                parts = stripped.split(maxsplit=2)
                if len(parts) == 3:
                    flag = parts[1]
                    value = parts[2]
                    config["slurm"][flag] = value
                elif len(parts) == 2:
                    # Handles flags like "--exclusive" without a value
                    config["slurm"][parts[1]] = True
            elif stripped and not stripped.startswith("#"):
                config["prologue"].append(stripped)

    return config


def create_slurm_cluster(njobs:int, slurm_config:str):
    config = parse_slurm_config(slurm_config)
    cluster = SLURMCluster(queue=config["slurm"].get("--partition", "cpu"), # SLURM partition
                          cores=config["slurm"].get("--cpus", 1),
                          memory=config["slurm"].get("--mem", "1G"),
                          walltime=config["slurm"].get("--time", "01:00:00"))
    cluster.scale(jobs=njobs) # Launch one job per system
    return cluster

def run_cp2k(calc):
    try:
      os.chdir(calc.working_directory)
      calc.run()
      return(os.getcwd())
    except Exception as e:
      return(f"Error: {e}")
    

if __name__ == "__main__":
    args = parse()
    # Load and preprocess dataset
    ds = load_dataset(args.dataset)
    symbols_set = get_elements(ds)
    ds = add_isolated_atoms(ds, symbols_set)

    root_dir=os.getcwd()
    calcs=[]
    for i, system in enumerate(ds):
        system.info["index"] = f"system_{i}"
        system_dir=os.path.join(root_dir,ds[i].info["index"])
        os.makedirs(system_dir,exist_ok=True) 
        calc=CP2K(cp2k_command=args.cp2k_command,project_name=system.info["index"],run_type="ENERGY_FORCE",working_directory=system_dir)
        calc.atoms = system
        if args.method == "xtb":
            add_xTB_OT(atoms=system,calc=calc,charge=system.info.get("charge",0),LSD=system.info["oddNumberofElectrons"],Ignore_convergence_failure=True,max_scf=1,outer_max_scf=0)
        elif args.method == "pbe":
            add_PBE_OT(atoms=system,calc=calc,charge=system.info.get("charge",0),LSD=system.info["oddNumberofElectrons"],Ignore_convergence_failure=True,max_scf=1,outer_max_scf=0)
        calc.forces_path=add_print_singlepoint_forces(calc=calc,filename="forces",unit="EV/ANGSTROM")
        calc.stress_path=add_print_stress_tensor(calc=calc,filename="./",unit="EV/ANGSTROM^3")
        calc.calcs.append(calc)

    cluster=create_slurm_cluster(njobs=len(ds), slurm_config=args.slurm_config)
    with Client(cluster) as client:
        futures = client.map(run_cp2k, calcs)
        results = client.gather(futures)
    
    #Postprocessing
    for calc in calcs:
        calc.atoms.info["E"]=postprocess_energy(calc=calc)
        calc.atoms.set_array("forces",postprocess_forces(forces_path=calc.forces_path))
        calc.atoms.info["stress"]=postprocess_stress(stress_path=calc.stress_path,notation="voigt")
    results= [calc.atoms for calc in calcs]
    write(args.output, results, format="extxyz", append=True)
    print(f"Dataset written to {args.output}")