from ase import Atoms
from pycp2k.templates.GLOBAL.GLOBAL import CP2K
import numpy as np

##################################################################################
#                                     ENERGY                                     #
##################################################################################

def add_print_singlepoint_energy(calc:CP2K,filename:str="energy",unit:str=None):
    """
    Add a print section to FORCE_EVAL that prints the energy to a file
    """
    raise NotImplementedError("print_singlepoint_energy is not in use.")

def postprocess_energy(calc: CP2K):
    """
    Parse the CP2K stdout for the converged value of the energy, return as a float
    """
    cp2k_output_path=f"{calc.CP2K_INPUT.GLOBAL.Project_name}.out"
    switch=False
    total_energy=None
    with open(cp2k_output_path,"r") as f:
        for line in f:
            if "Total energy:" in line:
                line=line.split()
                total_energy=float(line[2])
    if total_energy is None:
        raise ValueError(f"Total energy not found in {cp2k_output_path}")
    return total_energy

##################################################################################
#                                     FORCES                                     #
##################################################################################


def add_print_singlepoint_forces(calc:CP2K,filename:str="forces", unit:str=None):
    '''
    Add a print section to FORCE_EVAL that prints the forces to a file
    '''
    PRINT_FORCES=calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES
    if unit is not  None:
       PRINT_FORCES.Force_unit=unit
    PRINT_FORCES.Filename=filename
    PRINT_FORCES.EACH.Just_energy=1
    full_filename=f"{calc.project_name}-{PRINT_FORCES.Filename}-1_0.xyz"
    print(f"converged forces will be printed to {full_filename}")
    return full_filename

def postprocess_forces(forces_path: str):
    """
    Parse the forces output file, return as a np.array
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
    return np.array(forces)

##################################################################################
#                                     STRESS                                     #
##################################################################################

def add_print_stress_tensor(calc:CP2K,filename:str="stress",unit:str=None):
    """
    Add a PRINT section to FORCE_EVAL that prints the stress tensor to a file
    """
    calc.CP2K_INPUT.FORCE_EVAL_list[0].Stress_tensor="ANALYTICAL"
    PRINT_STRESS_TENSOR=calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.STRESS_TENSOR
    PRINT_STRESS_TENSOR.EACH.Just_energy=1
    PRINT_STRESS_TENSOR.Filename="./"
    if unit is not None:
        PRINT_STRESS_TENSOR.Stress_unit=unit
    full_filename=f"{calc.project_name}-1_0.stress_tensor"
    return full_filename

def postprocess_stress(stress_path: str, notation: str="voigt"):
    """
    Parse the stress output file and return the stress tensor as a np.array
    """
    notation_types=["full","voigt"]
    if notation not in notation_types:
        raise(f"Stress notation can only be one of the following options: {notation_types}")
    parse=False
    stress_tensor=[]
    with open(stress_path,"r") as f:
        for line in f:
            line=line.split()
            if line==["STRESS|","x","y","z"]:
                parse=True
            elif line[0:3]==["STRESS|","1/3","Trace"]:
                parse=False
            elif parse==True:
                stress_tensor.append([float(i) for i in line[2:5]])
    stress_tensor=np.array(stress_tensor)
    
    if notation=="full":
       return stress_tensor
    if notation=="voigt":
       return np.array([stress_tensor[0,0],stress_tensor[1,1],stress_tensor[2,2],stress_tensor[1,2],stress_tensor[0,2],stress_tensor[0,1]])