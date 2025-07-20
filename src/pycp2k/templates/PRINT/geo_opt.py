from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from ase.io import read, write

def add_print_geo_opt(calc: CP2K, **kwargs):
    """
    Set up a print section in the cp2k input file to print coordinates, energy and forces after every N geometry optimization steps
    """
    allowed_kwargs=["each", "stress"]
    for kw in kwargs:
        if kw not in allowed_kwargs:
            raise ValueError(f"Invalid keyword: {kw}")
        
    stress=kwargs.get("stress", False)
    if stress:
        calc.CP2K_INPUT.FORCE_EVAL_list[0].Stress_tensor=kwargs.get("stress", "ANALYTICAL")
        calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.STRESS_TENSOR.EACH.Just_energy=kwargs.get("each", 1)
        calc.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.STRESS_TENSOR.Filename="./"

    calc.CP2K_INPUT.MOTION.PRINT_add()
    PRINT=calc.CP2K_INPUT.MOTION.PRINT_list[0]
    each=kwargs.get("each", 1)
    PRINT.TRAJECTORY.EACH.Geo_opt=each
    PRINT.FORCES.EACH.Geo_opt=each

def postprocess_geo_opt(calc: CP2K, **kwargs):

    # Step 0 (original coordinates and forces) are not printed. Need to think how to handle this.
    pos_file=kwargs.get("pos_file",f"{calc.CP2K_INPUT.GLOBAL.Project_name}-pos-1.xyz")
    frc_file=kwargs.get("frc_file",f"{calc.CP2K_INPUT.GLOBAL.Project_name}-frc-1.xyz")
    pos=read(pos_file,":")
    frc=read(frc_file,":")
    for i in range(len(pos)):
        pos[i].arrays["frc"]=frc[i].get_positions()
    write(f"{calc.CP2K_INPUT.GLOBAL.Project_name}.xyz",pos,format="extxyz")
    return


