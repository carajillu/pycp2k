from ase import Atoms
import time
def return_performance_meter(atoms: Atoms,dyn):
    def performance_meter():
            atoms.info["step"]=dyn.nsteps
            if not hasattr(atoms, "time0"):
               atoms.time0=time.perf_counter()      
            atoms.info["elapsed"]=time.perf_counter()-atoms.time0
    return performance_meter