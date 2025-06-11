from ase import Atoms
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
import numpy as np

def add_print_singlepoint(calc:CP2K,**kwargs):
    kwargs_keys=["filename","each_just_energy", "forces", "stress"]
    for key in kwargs.keys():
        if key not in kwargs_keys:
            raise ValueError(f"{key} is not a valid keyword argument for add_print_forces, valid arguments are {kwargs_keys}")
        
    stress=kwargs.get("stress", False)
    if stress:
        calc.CP2K_INPUT.FORCE_EVAL_list[0].Stress_tensor=kwargs.get("stress", "ANALYTICAL")
        calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.STRESS_TENSOR.EACH.Just_energy=kwargs.get("each_just_energy",1)
        calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.STRESS_TENSOR.Filename="./"
        
    PRINT_FORCES=calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES
    PRINT_FORCES.Filename=kwargs.get("filename","forces")
    PRINT_FORCES.EACH.Just_energy=kwargs.get("each_just_energy",1)
    print(f"forces will be printed to {PRINT_FORCES.Filename}")
    print(f"forces will be printed every {PRINT_FORCES.EACH.Just_energy} steps")
    return

def postprocess(calc:CP2K,atoms:Atoms,**kwargs):
    # Postprocess energy

    # Postprocess forces
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

    # Postprocess stress
    stress_filename=kwargs.get("filename","./")
    stress_path=f"{stress_filename}{calc.project_name}-1_0.stress_tensor"
    with open(stress_path,"r") as f:
        for line in f:
            line=line.split()
            if line[0:2]==['STRESS|', 'Sum']:
                parse=False
            if parse:
                stress.append([float(i) for i in line[2:5]])
    return