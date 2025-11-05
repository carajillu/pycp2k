from pycp2k.templates.PRINT.singlepoint import *
from copy import deepcopy
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from dask.distributed import Client
from ase import Atoms


def return_cp2k_dask_singlepoint(atoms: Atoms, cp2k_calc:CP2K,client:Client,label:str="cp2k"):
    """
    This function will be attached to the ASE MD object.
    """
    def run_cp2k_singlepoint(cp2k_calc_dask):
        cp2k_calc_dask.run()
        cp2k_calc_dask.atoms.info["cp2k_energy"]=postprocess_energy(calc=cp2k_calc_dask)
        cp2k_calc_dask.atoms.set_array("cp2k_forces",postprocess_forces(forces_path=cp2k_calc_dask.forces_path))
        cp2k_calc_dask.atoms.info["cp2k_stress"]=postprocess_stress(stress_path=cp2k_calc_dask.stress_path,notation="voigt")
        return deepcopy(cp2k_calc_dask.atoms)
    def cp2k_dask():
        if not hasattr(atoms,"futures"):
            atoms.futures=[]
        idx=len(atoms.futures)
        cp2k_calc_dask=deepcopy(cp2k_calc)
        atoms4dask=deepcopy(atoms)
        atoms4dask.calc=None
        cp2k_calc_dask.project_name=f"{label}_{idx}"
        cp2k_calc_dask.working_directory=f"results/{label}_{idx}"
        cp2k_calc_dask.atoms=atoms4dask
        cp2k_calc_dask.forces_path=add_print_singlepoint_forces(calc=cp2k_calc_dask,filename="forces",unit="EV/ANGSTROM")
        cp2k_calc_dask.stress_path=add_print_stress_tensor(calc=cp2k_calc_dask,filename=f"./",unit="EV/ANGSTROM^3")
        print(f"Submitting CP2K calculation via dask")
        fut=client.submit(run_cp2k_singlepoint,cp2k_calc_dask,pure=False,key=f"{label}_{idx}") #key might be useful later
        atoms.futures.append(fut)
    return cp2k_dask