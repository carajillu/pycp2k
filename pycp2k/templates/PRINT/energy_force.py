from ase import Atoms
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
import numpy as np

def add_print_forces(calc:CP2K,**kwargs):
    kwargs_keys=["filename","each_just_energy"]
    for key in kwargs.keys():
        if key not in kwargs_keys:
            raise ValueError(f"{key} is not a valid keyword argument for add_print_forces, valid arguments are {kwargs_keys}")
    PRINT_FORCES=calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES

    PRINT_FORCES.Filename=kwargs.get("filename","forces.out")
    PRINT_FORCES.EACH.Just_energy=kwargs.get("each_just_energy",1)
    return

def postprocess_forces(calc:CP2K,atoms:Atoms,**kwargs):
    forces_filename=kwargs.get("filename","forces.out")
    forces_path=f"{calc.project_name}-{forces_filename}-1_0.xyz"
    """
    Need to read the forces output and add it as an array property to the atoms object
    """
    parse=False
    forces=[]
    with open(forces_path,"r") as f:
        for line in f:
            line=line.split()
            if line[0:2]==['FORCES|', 'Sum']:
                parse=False
            if parse:
                forces.append([float(i) for i in line[2:5]])
            if line==['FORCES|', 'Atom', 'x', 'y', 'z', '|f|']:
                parse=True
    atoms.set_array("forces",np.array(forces))
    return