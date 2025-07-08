from ase import Atoms
from ase.io import read, write
import argparse
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.xTB_templates import add_xTB_OT
from pycp2k.templates.FORCE_EVAL.PBE_templates import add_PBE_OT
from pycp2k.templates.PRINT.singlepoint import *
import subprocess

def parse():
    parser=argparse.ArgumentParser()
    parser.add_argument("--structures",type=str,default="structures.xyz")
    parser.add_argument("--output",type=str,default="mace_ds.xyz")
    args=parser.parse_args()
    return args

def load_dataset(path: str) -> list[Atoms]:
    structures=read(path,index=":")
    for structure in structures:
        charge=structure.info.get("charge",0)
        total_electrons = sum(structure.get_atomic_numbers()) - charge
        structure.info["oddNumberofElectrons"]=total_electrons%2==1
    return structures

def get_elements(structures: list[Atoms]) -> set[str]:
    # Get all unique elements
    symbols_set = set()
    for structure in structures:
        symbols_set.update(structure.get_chemical_symbols())
    print(f"Elements present in dataset: {symbols_set}")
    return symbols_set

def add_isolated_atoms(structures: list[Atoms],symbols_set: list[str]) -> set[Atoms]:
    #Generate isolated atom objects and prepend to dataset
    isolated_atoms=[]
    for symbol in symbols_set:
        atoms_i=Atoms(symbols=[symbol], positions=[[0, 0, 0]],info={"config_type":"IsolatedAtom"},cell=np.array([5.,5.,5.]))
        atoms_i.info["oddNumberofElectrons"]=atoms_i.get_atomic_numbers()[0]%2==1
        isolated_atoms.append(atoms_i)
    return isolated_atoms+structures

def mk_mace_dataset(ds: list[Atoms]):
    symbols_set=get_elements(ds)
    ds=add_isolated_atoms(ds,symbols_set)
    for system in ds:
        print(system, system.info)
    
    nfailed=0
    for system in ds:
        print(system, system.info)
        calc=CP2K(project_name="mace_xTB",run_type="ENERGY_FORCE") # Need to redefine calculator every time?
        add_xTB_OT(atoms=system,calc=calc,charge=system.info.get("charge",0),LSD=system.info["oddNumberofElectrons"])
        #add_PBE_OT(atoms=system,calc=calc,charge=system.info.get("charge",0),LSD=system.info["oddNumberofElectrons"])
        forces_path=add_print_singlepoint_forces(calc=calc,filename="forces")
        stress_path=add_print_stress_tensor(calc=calc,filename="./")
        try:
            calc.run()
        except Exception as e:
            print(f"Error: {e}")
            output_file=f"{calc.project_name}.out"
            subprocess.run(["tail", "-n", "30", output_file])
            nfailed+=1
            continue
        system.info["E"]=postprocess_energy(calc=calc)
        system.set_array("forces",postprocess_forces(forces_path=forces_path))
        system.info["stress"]=postprocess_stress(stress_path=stress_path,notation="voigt")
        calc.cleanup(quiet=True)

    print(f"Number of failed calculations: {nfailed}")
    return ds

if __name__=="__main__":
    args=parse()
    structures=load_dataset(args.structures)
    ds=mk_mace_dataset(structures)
    write(args.output,ds,format="extxyz")
