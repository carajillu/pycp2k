from ase import Atoms
import random

def remove_random_atom(atoms: Atoms, element: str=None):
    symbols=atoms.get_chemical_symbols()
    if element is not None:
       element_indices=[i for i in range(0,len(symbols)) if symbols[i]==element]
    else:
        element_indices=symbols
        assert len(element_indices)>0, f"Atoms object does not seem to have any {element} atoms"
    new_atoms=atoms.copy() 
    del(new_atoms[random.choice(element_indices)])
    return new_atoms
    

