from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.DFT.xTB import add_xTB
from pycp2k.templates.FORCE_EVAL.SCF.OT import add_SCF_OT
from pycp2k.templates.FORCE_EVAL.SUBSYS.add_atoms import add_coords,add_cell
from ase import Atoms

def add_xTB_OT(atoms:Atoms,calc:CP2K,**kwargs):
    calc.CP2K_INPUT.FORCE_EVAL_add()
    add_xTB(atoms=atoms,calc=calc,**kwargs)
    add_SCF_OT(calc=calc,**kwargs)
    add_coords(atoms=atoms,calc=calc)
    add_cell(atoms=atoms,calc=calc)
    return
