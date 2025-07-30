from ase import Atoms
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
import numpy as np

def add_coords(atoms:Atoms,calc:CP2K):
    #Adds the coordinates section to a calculator containing a SUBSYS section
    default_keyword=[]
    for i in range(len(atoms)):
        default_keyword.append(atoms[i].symbol+" "+" ".join(map(str, atoms.positions[i])))
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.COORD.Default_keyword=default_keyword
    return

def add_cell(atoms:Atoms,calc:CP2K):
    #Adds the cell section to a calculator containing a SUBSYS section
    if not atoms.cell:
       # find maximum and minimum coordinates in each direction.
       atoms.center()
       max_coords=atoms.positions.max(axis=1)
       min_coords=atoms.positions.min(axis=1)
       cell_lengths=max_coords-min_coords
       atoms.cell=np.array([[cell_lengths[0],0,0],[0,cell_lengths[1],0],[0,0,cell_lengths[2]]])
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.A=" ".join(map(str, atoms.cell[0]))
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.B=" ".join(map(str, atoms.cell[1]))
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.C=" ".join(map(str, atoms.cell[2]))
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.Periodic="XYZ"
    print(f"Cell: {atoms.cell}")
    return