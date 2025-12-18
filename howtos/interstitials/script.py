import functools
print = functools.partial(print, flush=True) # all print()s will be called with "flush=True"
print("import os, sys, argparse, glob"); import os, sys, argparse, glob
print("from ase import Atoms"); from ase import Atoms
print("from ase.io import read, write");from ase.io import read, write
print("from pycp2k.templates.GLOBAL.GLOBAL import CP2K");from pycp2k.templates.GLOBAL.GLOBAL import CP2K
print("from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT");from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
print("from pycp2k.ase_utils.interstitials import remove_random_atom"); from pycp2k.ase_utils.interstitials import remove_random_atom
print("from copy import copy, deepcopy"); from copy import copy, deepcopy
print("import pandas as pd, numpy as np"); import pandas as pd, numpy as np
print("import time"); import time
print("from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait"); from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
print("import subprocess"); import subprocess

def parse():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run CP2K calculations in parallel using Dask.")
    parser.add_argument("--input_structure", type=str, default="input.xyz", help="Input structure file.")
    parser.add_argument("--nreps",type=int,default=1,help="Number of copies of input_structure to run")
    parser.add_argument("--cp2k_command", type=str, default="cp2k.psmp")
    parser.add_argument("--cp2k_input", type=str, nargs="+", default=["input.inp"])
    parser.add_argument("--scale",type=int,default=1,help="Number of jobs to run at the same time")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()

def run_cp2k(calc):
    start=time.time()
    crdfilename=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz"
    wfn_restart=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-RESTART.wfn"
    # uncomment for testing
    #calc.wfn_restart=wfn_restart
    #end=time.time()
    #print(calc.project_name,calc.mpi_flags)
    #return calc, end-start
    # end uncomment for testing
    try:
       new_atoms=read(crdfilename,":")[-1]    
       calc.atoms=new_atoms
       if os.path.isfile(wfn_restart):
          calc.wfn_restart=wfn_restart
       return calc, 0.
    except Exception:
        try:
           if os.path.isfile(wfn_restart):
              calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Wfn_restart_file_name=wfn_restart
           calc.run()
           new_atoms=read(crdfilename,":")[-1]    
           calc.atoms=new_atoms
           calc.wfn_restart=wfn_restart
           end=time.time()
           return calc, end-start
        except Exception as e:
           print(f"Calculation {calc.run_id} of replicate {calc.rep_id} failed. See error message.")
           print(e)
           return calc, -1.

def build_cp2k_calc(cp2k_command:str, input_file:str, rep_id:int, run_id:int=0) -> CP2K:
    calc_i=CP2K(cp2k_command=cp2k_command)
    calc_i.rep_id=rep_id
    calc_i.run_id=run_id
    calc_i.parse(input_file)
    with open(input_file,"r") as f:
        for line in f:
            if line.startswith("#SBATCH"):
                calc_i.mpi_flags.append(line.split()[1])
            elif line.startswith("#EXPORT"):
                calc_i.mpi_flags.append(f"--export {line.split()[1]}")
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
    
    # Create DataFrame to track results
    calc_pd=pd.DataFrame({"Replicate":[f"rep_{j}" for j in range(args.nreps)]})
    for input_file in args.cp2k_input:
        calc_pd[input_file]=[None]*args.nreps

    # Build matrix of calculators
    calculation_matrix=[]
    for j in range(args.nreps):
        calc_j_lst=[]
        for i in range(len(args.cp2k_input)):
            calc_i=build_cp2k_calc(args.cp2k_command,input_file=args.cp2k_input[i],rep_id=j,run_id=i)
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
                #If this job has failed, we do not submit the next
                if runtime==-1.: 
                   continue
                print(f"Job at location: {completed_calculator.working_directory}: complete in {runtime} seconds")
                if completed_calculator.run_id<len(args.cp2k_input)-1:
                   next_calc=calculation_matrix[completed_rep_id][completed_run_id+1] # only referencing, no deepcopy
                   next_calc.run_id=completed_run_id+1
                   next_calc.atoms=completed_calculator.atoms
                   next_calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Wfn_restart_file_name=completed_calculator.wfn_restart
                   job=exe.submit(run_cp2k,next_calc)
                   not_done.add(job)
            done = []

    calc_pd.to_csv("timings.csv",header=True,index=False)