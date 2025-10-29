import argparse, os

from dask.distributed import Client, wait, as_completed

from mace.calculators import MACECalculator 

from ase.io import read, write
from ase.units import fs, kB
from ase.md import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import MDLogger

from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from pycp2k.templates.PRINT.singlepoint import *
#from pycp2k.dask_utils.archer2 import create_cluster
from pycp2k.dask_utils.local import create_cluster

from make_filaments import make_surface, find_cylinders, make_interstitial, find_neighbours

def parse():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run CP2K calculations in parallel using Dask.")
    parser.add_argument("--cp2k_command", type=str, default="cp2k.psmp")
    parser.add_argument("--cp2k_mpi_proc", type=int, default=1)
    parser.add_argument("--input_structure", type=str, default="input.xyz", help="Input structure file.")
    parser.add_argument("--nreps", type=int, default=1, help="Number of repetitions for the input structure.")
    parser.add_argument("--method", type=str, default="xtb", choices=["xtb", "pbe"], help="Method to use for calculations (xtb or pbe).")
    parser.add_argument("--slurm_config", type=str, default="slurm.sh", help="SLURM configuration file to use when creating dask cluster.")
    parser.add_argument("--slurm_scale",type=int,default=1,help="Number of SLURM nodes to spawn")
    parser.add_argument("--cp2k_mpi_processes",type=int,default=1,help="Number of MPI processes to run CP2K with")
    parser.add_argument("--output", type=str, default="ds_ready.xyz", help="Output file for the dataset.")
    return parser.parse_args()

def return_print_snapshot(basename):
    def print_snapshot():
        #atoms.arrays["forces"]=atoms.get_forces()
        atoms.arrays['node_energy']=atoms.calc.results['node_energy']
        atoms.info["E"]=atoms.calc.results["E"]
    return print_snapshot

def get_mace_quantities():
    atoms.info["mace_energy"]=atoms.calc.results["energy"]
    atoms.arrays['node_energy']=atoms.calc.results['node_energy']
    atoms.arrays['mace_forces']=atoms.calc.results['forces']
    atoms.info["stress"]=atoms.calc.results["stress"]

def return_cp2k_dask(client,cp2k_calc):
    def run_cp2k_singlepoint(cp2k_calc):
        cp2k_calc.run()
        atoms.info["cp2k_energy"]=postprocess_energy(calc=cp2k_calc)
        atoms.set_array("cp2k_forces",postprocess_forces(forces_path=cp2k_calc.forces_path))
        atoms.info["stress_cp2k"]=postprocess_stress(stress_path=cp2k_calc.stress_path,notation="voigt")
        return atoms.copy()
    def cp2k_dask():
        idx=len(atoms.futures)
        cp2k_calc.project_name=f"cp2k_{idx}"
        cp2k_calc.working_directory=f"results/cp2k_{idx}"
        atoms4dask=atoms.copy()
        atoms4dask.calc=None
        cp2k_calc.atoms=atoms4dask
        cp2k_calc.forces_path=add_print_singlepoint_forces(calc=cp2k_calc,filename="forces",unit="EV/ANGSTROM")
        cp2k_calc.stress_path=add_print_stress_tensor(calc=cp2k_calc,filename=f"./",unit="EV/ANGSTROM^3")
        print(f"Submitting CP2K calculation via dask")
        fut=client.submit(run_cp2k_singlepoint,cp2k_calc,pure=False,key=f"xtb_{idx}") #key might be useful later
        atoms.futures.append(fut)
    return cp2k_dask


def compare_mace_cp2k(atoms,basename):
    tol=1e-8
    differences=[]
    differences.append(abs(atoms.info["mace_energy"]-atoms.info["cp2k_energy"]))
    for i in range(0,len(atoms.arrays["positions"])):
        differences.append(abs(atoms.arrays["mace_forces"][i][0]-atoms.arrays["cp2k_forces"][i][0]))
        differences.append(abs(atoms.arrays["mace_forces"][i][1]-atoms.arrays["cp2k_forces"][i][1]))
        differences.append(abs(atoms.arrays["mace_forces"][i][2]-atoms.arrays["cp2k_forces"][i][2]))

    if any(element>tol for element in differences):
       print(f"adding snapshot to training set")
       write(f"{basename}_trj.xyz",atoms,format="extxyz",append=True)

if __name__=="__main__":
   
   #parse arguments
   args=parse()

   # Create the Atoms object
   atoms=read(args.input_structure)
   print(atoms)

   # create cp2k calculator, setup PBE and add the first atoms object (for potentials and basis sets)
   cp2k_calc=CP2K(run_type="ENERGY_FORCE",mpi_n_procs=args.cp2k_mpi_processes)
   add_PBE_OT(atoms=atoms, calc=cp2k_calc,
           feval_idx=0,
           preconditioner="FULL_ALL",minimizer="DIIS", # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.OT.add_OT
           scf_guess="ATOMIC",max_scf=200,eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_inner_SCF
           outer_max_scf=20,outer_eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_outer_SCF
           Ignore_convergence_failure=True,
           )

   # Create MACE calculator and assign it to Atoms object
   mace_calc=MACECalculator(model_path="mace-mpa-0-medium.model",device="cpu")
   atoms.calc=mace_calc


   # Create the dask cluster with dynamic scaling, add futures list to the Atoms object
   cluster=create_cluster(slurm_config=args.slurm_config)
   cluster.adapt(minimum=2, maximum=20)
   #cluster=create_cluster()
   #cluster.scale(1)
   client=Client(cluster)
   atoms.futures=[]

   # Setup MD calculation
   dyn=Langevin(atoms=atoms, timestep=1*fs, temperature_K=300, friction=0.01)
   Logger=MDLogger(dyn=dyn,atoms=atoms, logfile="log.txt", header=True, stress=False, peratom=False, mode="w")
   cp2k_dask=return_cp2k_dask(client,cp2k_calc)
   dyn.attach(Logger,interval=1000)
   dyn.attach(get_mace_quantities, interval=1000)
   dyn.attach(cp2k_dask,interval=1000)
   dyn.run(1e+6)

   for future in as_completed(atoms.futures):
       try:
           snapshot=future.result()
           compare_mace_cp2k(snapshot,"training")
       except Exception as e:
           print(f"Task {future.key} failed with error {e}")
       
   systems=[]
   wait(atoms.futures)
   for future in atoms.futures:
       print(future.result(),type(future.result()))
       systems.append(future.result())
   write("result.xyz",systems,format="extxyz")