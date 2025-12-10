import functools
print = functools.partial(print, flush=True) # all print()s will be called with "flush=True"
print("import os, sys, argparse"); import os, sys, argparse
print("from ase import Atoms"); from ase import Atoms
print("from ase.io import read, write");from ase.io import read, write
print("from pycp2k.templates.GLOBAL.GLOBAL import CP2K");from pycp2k.templates.GLOBAL.GLOBAL import CP2K
print("from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT");from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
print("from pycp2k.ase_utils.interstitials import remove_random_atom"); from pycp2k.ase_utils.interstitials import remove_random_atom
print("from copy import copy, deepcopy"); from copy import copy, deepcopy
print("import pandas as pd"); import pandas as pd
print("import time"); import time
print("from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait"); from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
print("import subprocess"); import subprocess

def parse():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run CP2K calculations in parallel using Dask.")
    parser.add_argument("--input_structure", type=str, default="input.xyz", help="Input structure file.")
    #parser.add_argument("--water",action="store_true",help="Debugging run with a water molecule")
    parser.add_argument("--nreps",type=int,default=1,help="Number of copies of input_structure to run")
    parser.add_argument("--cp2k_command", type=str, default="cp2k.psmp")
    parser.add_argument("--cp2k_mpi_processes",type=int,default=1,help="Number of MPI processes to run CP2K with")
    parser.add_argument("--cp2k_nodes",type=int,default=None,help="Number of nodes to run CP2K on")
    parser.add_argument("--cp2k_omp_threads",type=int,default=1,help="Number of OMP threads for each MPI rank used by CP2K (will be set at system level with os.environ)")
    parser.add_argument("--dask_scale",type=int,default=1,help="Number of DASK jobs to spawn")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()

def run_cp2k(calc):
    start=time.time()
    write(f"{calc.working_directory}/initial_structure.xyz",calc.atoms)
    calc.run()
    crdfilename=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz"
    new_atoms=read(crdfilename,":")[-1]
    new_atoms.info["run_name"]=calc.atoms.info["run_name"]
    calc.atoms=new_atoms
    end=time.time
    return calc, end-start

def get_new_calc(calc:CP2K,atoms:Atoms,project_name:str):
    new_calc=copy(calc) #not deepcopy cause we need a shared list of nodes
    new_calc.project_name=project_name
    new_calc.CP2K_INPUT.GLOBAL.Project_name=new_calc.project_name #use a setter for that in the future?
    new_calc.atoms=atoms
    new_calc.working_directory=f"{new_calc.working_directory}/results/{new_calc.atoms.info["run_name"]}/{new_calc.project_name}"
    return new_calc


def get_new_calc_lst(calc:CP2K,atoms_lst:list[Atoms]):
    new_calcs=[]
    for i, atoms in enumerate(atoms_lst):
        project_name=f"{calc.project_name}_{i}"
        new_calc_i=get_new_calc(calc=calc,atoms=atoms,project_name=project_name)
        new_calcs.append(new_calc_i)
    return new_calcs


if __name__=="__main__":
    print("Program started")

    # Parse arguments
    args=parse()

    # Get atoms
    atoms=read(args.input_structure)

    # Construct the base PBE calculator
    calc=CP2K(input_file="int_0_PBE.inp",mpi_n_procs=args.cp2k_mpi_processes)
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL.PBE.Scale_c=1 # Adding explicit default value, this is because pycp2k ignores empty sections, but CP2K wants them sometimes
    if args.cp2k_nodes is not None:
       calc.mpi_flags.append(f"--nodes={args.cp2k_nodes}")
       calc.mpi_flags.append(f"--ntasks-per-node={int(args.cp2k_mpi_processes/args.cp2k_nodes)}")
       calc.mpi_flags.append(f"--exclusive")
    
    # Construct the set of Atoms objects with random oxygen atoms removed
    new_atoms=[]
    for i in range(args.nreps):
        atoms_i=remove_random_atom(atoms,element="O")
        atoms_i.info["run_name"]=f"system_{i}"
        new_atoms.append(atoms_i)
    new_calcs=get_new_calc_lst(calc,new_atoms)

    # Submit jobs in parallel (?)
    not_done=set()
    with ThreadPoolExecutor(max_workers=args.dask_scale) as exe:
        for calc in new_calcs:
            job=exe.submit(run_cp2k,calc)
            not_done.add(job)

    # Wait for job(s) to complete and generate any new jobs
    while len(not_done) > 0:
        done, not_done = wait(not_done, return_when=FIRST_COMPLETED)
        print(f"{len(done)} task(s) completed")

        for job in done:
            run_id, runtime = job.result()
            print(f"Job {run_id} complete in {runtime} seconds")

            # Check runtime - if many jobs are failing fast, then should quit the whole job.
            # Lots of quickly generated job steps can overload SLURM (affecting other users), so
            # we want to avoid that.

            # Process results and/or submit new job(s)

        done = []