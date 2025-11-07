from ase.io import read
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from dask.distributed import Client, wait, as_completed
from pycp2k.dask_utils.local import create_cluster
from pycp2k.ase_utils.interstitials import remove_random_atom
from copy import deepcopy

def run_cp2k(calc):
    calc.run()
    #get the optimised coordinates
    return calc
    return 0


if __name__=="__main__":
    #Create Dask local cluster
    cluster=create_cluster(scale=2)
    client=Client(cluster)
    

    calc=CP2K(input_file="int_0_PBE.inp")
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL.PBE.Scale_c=1 # Adding explicit default value, this is because pycp2k ignores empty sections, but CP2K wants them sometimes
    calc.mpi_n_processes=4

    atoms=read("CR100_10.xyz")
    new_calcs=[]
    for i in range(5):
        new_calc=deepcopy(calc)
        new_calc.project_name=f"{calc.project_name}_{i}"
        new_calc.CP2K_INPUT.GLOBAL.Project_name=new_calc.project_name #use a setter for that in the future?
        new_calc.working_directory=f"{calc.working_directory}/{new_calc.project_name}"
        new_calc.atoms=remove_random_atom(atoms,element="O")
        new_calcs.append(new_calc)
    
    futures=client.map(run_cp2k,new_calcs)
    for fut in as_completed(futures):
        try:
         print(f"{fut.status}: {fut.result.project_name}")
        except AttributeError:
         print(fut.status)
    

    
    