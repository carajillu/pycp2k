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
    parser.add_argument("--cp2k_input", type=str, nargs="+", default=["input.inp"])
    parser.add_argument("--cp2k_mpi_processes",type=int,default=1,help="Number of MPI processes to run CP2K with")
    parser.add_argument("--cp2k_nodes",type=int,default=None,help="Number of nodes to run CP2K on")
    parser.add_argument("--cp2k_omp_threads",type=int,default=1,help="Number of OMP threads for each MPI rank used by CP2K (will be set at system level with os.environ)")
    parser.add_argument("--scale",type=int,default=1,help="Number of jobs to run at the same time")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()

def run_cp2k(calc):
    start=time.time()
    write(f"{calc.working_directory}/initial_structure.xyz",calc.atoms)
    calc.write_input_file()
    calc.run()
    crdfilename=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz"
    new_atoms=read(crdfilename,":")[-1]
    new_atoms.info["run_name"]=calc.atoms.info["run_name"]
    calc.atoms=new_atoms
    calc.wfn_restart=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-RESTART.wfn"
    end=time.time()
    return calc, end-start

def build_cp2k_calc(calc:CP2K, input_file:str, rep_id:int, run_id:int=0) -> CP2K:
    calc_i=deepcopy(calc)
    calc_i.rep_id=rep_id
    calc_i.run_id=run_id
    calc_i.parse(input_file)
    calc_i.project_name=calc_i.CP2K_INPUT.GLOBAL.Project_name
    calc_i.working_directory=f"run_{rep_id}/{calc_i.CP2K_INPUT.GLOBAL.Project_name}"
    try:
        calc_i.write_input_file()
    except Exception as e:
        print(f"Error writing input file: {e}")
    return calc_i


if __name__=="__main__":
    print("Program started")

    # Parse arguments
    args=parse()
    print(args)
     
    # Get atoms
    atoms=read(args.input_structure)

    # Construct the base CP2K calculator
    calc=CP2K(cp2k_command=args.cp2k_command,mpi_n_procs=args.cp2k_mpi_processes)
    if args.cp2k_nodes is not None:
       calc.mpi_flags.append(f"--nodes={args.cp2k_nodes}")
       calc.mpi_flags.append(f"--ntasks-per-node={int(args.cp2k_mpi_processes/args.cp2k_nodes)}")
       calc.mpi_flags.append(f"--exclusive")
    
    # Create DataFrame to track results
    calc_pd=pd.DataFrame({"Replicate":[f"rep_{j}" for j in range(args.nreps)]})
    for input_file in args.cp2k_input:
        calc_pd[input_file]=[None]*args.nreps

    # Build matrix of calculators
    calculation_matrix=[]
    for j in range(args.nreps):
        calc_j_lst=[]
        for i in range(len(args.cp2k_input)):
            calc_i=build_cp2k_calc(calc=calc,input_file=args.cp2k_input[i],rep_id=j)
            if i==0:
              atoms_i=remove_random_atom(atoms=atoms,element="O")
              calc_i.atoms=atoms_i
            calc_j_lst.append(calc_i)
        calculation_matrix.append(calc_j_lst)
            

    
    # Submit calculator i=0 for each j
    not_done=set()
    with ThreadPoolExecutor(max_workers=args.scale) as exe:
        for j in range(args.nreps):
            job=exe.submit(run_cp2k,calculation_matrix[j][0])
            not_done.add(job)

        # Wait for job(s) to complete and generate any new jobs
        while len(not_done) > 0:
            done, not_done = wait(not_done, return_when=FIRST_COMPLETED)
            print(f"{len(done)} task(s) completed")

            for job in done:
                completed_calculator, runtime = job.result()
                completed_run_id=completed_calculator.run_id # index i
                completed_rep_id=completed_calculator.rep_id # index j
                calc_pd.loc[completed_rep_id,args.cp2k_input[completed_run_id]]=runtime # correct syntax in pd 3.0
                print(f"Job at location: {completed_calculator.working_directory}: complete in {runtime} seconds")
                if completed_calculator.run_id<len(args.cp2k_input)-1:
                   next_calc=calculation_matrix[completed_rep_id][completed_run_id+1] # only referencing, no deepcopy
                   next_calc.run_id=completed_run_id+1
                   next_calc.atoms=completed_calculator.atoms
                   next_calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Wfn_restart_file_name=completed_calculator.wfn_restart
                   job=exe.submit(run_cp2k,next_calc)
                   not_done.add(job)
                # Check runtime - if many jobs are failing fast, then should quit the whole job.
                # Lots of quickly generated job steps can overload SLURM (affecting other users), so
                # we want to avoid that.
                # Process results and/or submit new job(s)
            done = []

    calc_pd.to_csv("timings.csv",header=True,index=False)