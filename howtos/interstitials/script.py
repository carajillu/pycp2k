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
      write(f"{calc.working_directory}/initial_structure.xyz",calc.atoms)
      calc.run()
      crdfilename=f"{calc.working_directory}/{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz"
      new_atoms=read(crdfilename,":")[-1]
      new_atoms.info["run_name"]=calc.atoms.info["run_name"]
      calc.atoms=new_atoms
    except:
      pass
    finally:
      return calc

def get_new_calc(calc:CP2K,atoms:Atoms,project_name:str):
    new_calc=deepcopy(calc)
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
        atoms_i=remove_random_atom(atoms,element="O")
        atoms_i.info["run_name"]=f"system_{i}"
        new_atoms.append(atoms_i)
    new_calcs=get_new_calc_lst(calc,new_atoms)
    pbe_futures=client.map(run_cp2k,new_calcs)
    all_futures=set(pbe_futures)

    #PBE0 as PBE calculations end
    pbe0_futures=[]
    calc_pbe0=CP2K(input_file="int_0.inp")
    for fut in as_completed(pbe_futures):
        calc_pbe=fut.result()
        if calc_pbe.calc_run_ok:
            atoms=calc_pbe.atoms
            pbe_idx=calc_pbe.project_name.split("_")[-1]
            calc_pbe0_i=get_new_calc(calc=calc_pbe0,atoms=atoms,project_name=f"{calc_pbe0.project_name}_{pbe_idx}")
            calc_pbe0_i.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Wfn_restart_file_name=f"../{calc_pbe.project_name}/{calc_pbe.project_name}-RESTART.wfn"
            pbe0_future=client.submit(run_cp2k,calc_pbe0_i)
            all_futures.add(pbe0_future)


    # Performance analysis
    calc_names=[]
    run_ok_status=[]
    nodes=[]
    mpi_ranks=[]
    omp_threads=[]
    time_exec=[]
    for fut in as_completed(all_futures):
        calc=fut.result()
        calc_names.append(calc.project_name)
        run_ok_status.append(calc.calc_run_ok)
        mpi_ranks.append(calc.mpi_n_processes)
        omp_threads.append(args.cp2k_omp_threads)
        time_exec.append(calc.last_exec_time)

    #wait for all futures, then print performance analysis
    wait(all_futures)
    z=pd.DataFrame({"name":calc_names,"run_ok": run_ok_status,"mpi_processes": mpi_ranks, "omp_threads": omp_threads,"last_exec_time":time_exec})
    z.to_csv("timings.csv",index=False)

    #write atoms to results file
    pbe0_atoms=[]
    for fut in pbe_futures:
        calc=fut.result()
        if "PBE0" in calc.project_name and calc.calc_run_ok:
            print(calc.project_name, calc.CP2K_INPUT.GLOBAL.Project_name)
            pbe0_atoms.append(calc.atoms)
    if len(pbe0_atoms)>0:
       write("result.xyz",pbe0_atoms,format="extxyz")

    # Close Dask cluster (I tend to forget)
    client.close()