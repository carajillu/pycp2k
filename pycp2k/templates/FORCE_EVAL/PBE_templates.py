from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from pycp2k.templates.FORCE_EVAL.DFT.PBE import add_PBE
from pycp2k.templates.FORCE_EVAL.DFT.SCF.OT import add_OT
from pycp2k.templates.FORCE_EVAL.DFT.SCF.loop import add_inner_scf,add_outer_scf
from pycp2k.templates.FORCE_EVAL.DFT.SCF.mixing import add_mixing
from pycp2k.templates.FORCE_EVAL.DFT.SCF.smear import add_smear
from pycp2k.templates.FORCE_EVAL.SUBSYS.add_atoms import add_coords,add_cell
from pycp2k.templates.FORCE_EVAL.SUBSYS.add_kinds import add_kinds
from ase import Atoms

def add_PBE_OT(atoms:Atoms,calc:CP2K,**kwargs):
    calc.CP2K_INPUT.FORCE_EVAL_add()
    add_PBE(calc=calc,**kwargs)
    add_OT(calc=calc,**kwargs)
    add_inner_scf(calc=calc,**kwargs)
    add_outer_scf(calc=calc,**kwargs)
    add_coords(atoms=atoms,calc=calc)
    add_cell(atoms=atoms,calc=calc)
    add_kinds(atoms=atoms,calc=calc,**kwargs)
    return

def add_PBE_mixing_smear(atoms:Atoms,calc:CP2K,**kwargs):
    calc.CP2K_INPUT.FORCE_EVAL_add()
    add_PBE(calc=calc,**kwargs)
    add_mixing(calc=calc,**kwargs)
    add_smear(calc=calc,**kwargs)
    add_coords(atoms=atoms,calc=calc)
    add_cell(atoms=atoms,calc=calc)
    add_kinds(atoms=atoms,calc=calc,**kwargs)
    return