import os, sys, argparse
from ase import Atoms
from ase.io import read, write
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from dask.distributed import Client, wait, as_completed
from pycp2k.dask_utils.local import create_cluster
from pycp2k.ase_utils.interstitials import remove_random_atom
from copy import deepcopy
from dask.distributed import wait
import pandas as pd

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
    try:
      calc.run()
      crdfilename=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz"
      calc.atoms=read(crdfilename,":")[-1]
    except:
      pass
    finally:
      return calc

def get_new_calcs(calc:CP2K,atoms_lst:list[Atoms]):
    new_calcs=[]
    for i, atoms in enumerate(atoms_lst):
        new_calc_i=deepcopy(calc)
        new_calc_i.project_name=f"{calc.project_name}_{i}"
        new_calc_i.CP2K_INPUT.GLOBAL.Project_name=new_calc_i.project_name #use a setter for that in the future?
        new_calc_i.working_directory=f"{calc.working_directory}/{new_calc_i.project_name}"
        new_calc_i.atoms=atoms
        new_calcs.append(new_calc_i)
    return new_calcs


if __name__=="__main__":
    #parse arguments
    args=parse()

    #Create Dask local cluster
    cluster=create_cluster(scale=args.dask_scale)
    client=Client(cluster)
    
    # Get atoms
    atoms=read(args.input_structure)

    #PBE
    os.environ["OMP_NUM_THREADS"]=str(args.cp2k_omp_threads)
    calc=CP2K(input_file="int_0_PBE.inp",mpi_n_procs=args.cp2k_mpi_processes)
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL.PBE.Scale_c=1 # Adding explicit default value, this is because pycp2k ignores empty sections, but CP2K wants them sometimes
    if args.cp2k_nodes is not None:
       calc.mpi_flags.append(f"--nodes={args.cp2k_nodes}")
       calc.mpi_flags.append(f"--ntasks-per-node={int(args.cp2k_mpi_processes/args.cp2k_nodes)}")

    new_atoms=[]
    for i in range(args.nreps):
        new_atoms.append(remove_random_atom(atoms,element="O"))
    new_calcs=get_new_calcs(calc,new_atoms)
    futures=client.map(run_cp2k,new_calcs)
    
    wait(futures)
    run_ok_status=[]
    nodes=[]
    mpi_ranks=[]
    omp_threads=[]
    time_exec=[]
    for fut in futures:
        calc=fut.result()
        run_ok_status.append(calc.calc_run_ok)
        mpi_ranks.append(calc.mpi_n_processes)
        omp_threads.append(args.cp2k_omp_threads)
        time_exec.append(calc.last_exec_time)
    
    z=pd.DataFrame({"run_ok": run_ok_status, "mpi_processes": mpi_ranks, "omp_threads": omp_threads,"last_exec_time":time_exec})
    print(z)
    client.close()
    sys.exit()

    # PBE0
    calc=CP2K(input_file="int_0.inp")
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL.PBE.Scale_c=1 # Adding explicit default value, this is because pycp2k ignores empty sections, but CP2K wants them sometimes
    calc.mpi_n_processes=12
    new_calcs=[]
    for i in range(len(pbe_atoms)):
        new_calc.project_name=f"{calc.project_name}_{i}"
        new_calc.CP2K_INPUT.GLOBAL.Project_name=new_calc.project_name #use a setter for that in the future?
        new_calc.working_directory=f"{calc.working_directory}/{new_calc.project_name}"
        new_calc.atoms=pbe_atoms[i]
        new_calcs.append(new_calc)

    futures=client.map(run_cp2k,new_calcs)
    wait(futures)
    pbe0_atoms=[]
    for fut in as_completed(futures):
        if fut.status=="finished":
           try:
              pbe0_atoms.append(fut.result())
           except:
              print(fut.result)
        else:
            print(fut.result)

    write("result.xyz",pbe0_atoms,format="extxyz")

    # Close Dask cluster (I tend to forget)
    client.close()