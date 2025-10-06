import os, sys, subprocess

from ase import Atoms
from ase.io import read,write

from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.xTB_templates import add_xTB_OT
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from pycp2k.templates.PRINT.singlepoint import *
from pycp2k.workflows.mk_mace_dataset import load_dataset,get_elements,add_isolated_atoms

from pycp2k.workflows.das.archer2 import parse_slurm_config, create_slurm_cluster

from dask_jobqueue import SLURMCluster
from dask.distributed import Client, wait

from make_filaments import make_surface, find_cylinders, make_interstitial, find_neighbours



def parse():
    """Parse command line arguments."""
    import argparse
    parser = argparse.ArgumentParser(description="Run CP2K calculations in parallel using Dask.")
    parser.add_argument("--cp2k_command", type=str, default="cp2k.psmp")
    parser.add_argument("--cp2k_mpi_proc", type=int, default=1)
    parser.add_argument("--input_structure", type=str, default="input.xyz", help="Input structure file.")
    parser.add_argument("--nreps", type=int, default=1, help="Number of repetitions for the input structure.")
    parser.add_argument("--method", type=str, default="xtb", choices=["xtb", "pbe"], help="Method to use for calculations (xtb or pbe).")
    parser.add_argument("--slurm_config", type=str, default="slurm.sh", help="SLURM configuration file to use when creating dask cluster.")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()


def run_cp2k(calc):
    try:
      os.chdir(calc.working_directory)
      calc.run()
      #cmd=f"srun -n {calc.mpi_n_processes} cp2k.psmp -i input.inp -o output.out"
      return(os.getcwd())
    except Exception as e:
      print(f"Error: {e}")
      return(f"Error: {e}")

def mk_dataset(input_structure: Atoms, nreps: int):
    ds=[]
    for i in range(nreps):
        surf = make_surface(atoms=atoms, vacuum=10.0)
        surf.info["interstitial_idx"]=find_neighbours(surf, center=surf.get_positions()[112], diameter=3.0)
        charge=surf.info.get("charge",0)
        total_electrons = sum(surf.get_atomic_numbers()) - charge
        surf.info["oddNumberofElectrons"]=total_electrons%2==1
        ds.append(surf)
    return ds    

if __name__ == "__main__":
    args = parse()
    # Load and preprocess dataset
    atoms= read(args.input_structure)
    ds=mk_dataset(atoms,args.nreps)
    symbols_set = get_elements(ds)
    ds = add_isolated_atoms(ds, symbols_set)

    root_dir=os.getcwd()
    calcs=[]
    for i, system in enumerate(ds):
        system.info["index"] = f"system_{i}"
        system_dir=os.path.join(root_dir,ds[i].info["index"])
        os.makedirs(system_dir,exist_ok=True) 
        calc=CP2K(cp2k_command=args.cp2k_command,project_name=system.info["index"],run_type="ENERGY_FORCE",working_directory=system_dir)
        calc.mpi_n_processes=args.cp2k_mpi_proc
        calc.mpi_on=True
        calc.mpi_command="srun"
        calc.atoms = system
        if args.method == "xtb":
            add_xTB_OT(atoms=system,calc=calc,charge=system.info.get("charge",0),LSD=system.info["oddNumberofElectrons"],Ignore_convergence_failure=True,max_scf=1,outer_max_scf=0)
        elif args.method == "pbe":
             add_PBE_OT(atoms=system, calc=calc,
                        feval_idx=0,
                        potential_file_name="POTENTIAL",basis_set_files=["BASIS_MOLOPT"],
                        preconditioner="FULL_ALL",minimizer="DIIS",
                        scf_guess="RESTART",max_scf=20,eps_scf=1e-6,
                        outer_max_scf=2,outer_eps_scf=1e-6,
                        potential="GTH-PBE", basis_set=["DZVP-MOLOPT-SR-GTH"],
                        LSD=system.info["oddNumberofElectrons"],Ignore_convergence_failure=True)
                       
        calc.forces_path=add_print_singlepoint_forces(calc=calc,filename="forces",unit=None)
        calc.stress_path=add_print_stress_tensor(calc=calc,filename="./",unit=None)
        calcs.append(calc)
        os.chdir(calc.working_directory)
        calc.write_input_file("input.inp")
        os.chdir(root_dir)

    cluster=create_slurm_cluster(njobs=len(ds), slurm_config=args.slurm_config)
    with Client(cluster) as client:
        futures = client.map(run_cp2k, calcs)
        wait(futures)
        results = client.gather(futures)
    
    #Postprocessing
    for calc in calcs:
        print(f"postprocessing system {calc.atoms.info['index']}")
        os.chdir(calc.working_directory)
        calc.atoms.info["E"]=postprocess_energy(calc=calc)
        if calc.atoms.info.get("config_type",None)=="IsolatedAtom":
            os.chdir(root_dir)  
            continue
        calc.atoms.set_array("forces",postprocess_forces(forces_path=calc.forces_path))
        calc.atoms.info["stress"]=postprocess_stress(stress_path=calc.stress_path,notation="voigt")
        os.chdir(root_dir)
    results= [calc.atoms for calc in calcs]
    write(args.output, results, format="extxyz", append=True)
    print(f"Dataset written to {args.output}")