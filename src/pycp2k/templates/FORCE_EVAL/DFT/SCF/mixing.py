from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_mixing(calc:CP2K,**kwargs):
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF
    SCF.MIXING.Method=kwargs.get("MIXING_Method","BROYDEN_MIXING")
    SCF.MIXING.Alpha=kwargs.get("MIXING_Alpha",0.6)
    SCF.MIXING.Beta=kwargs.get("MIXING_Beta",1.0)
    SCF.MIXING.Nbroyden=kwargs.get("MIXING_Nbroyden",15)
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING_Method: {SCF.MIXING.Method}")
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING_Alpha: {SCF.MIXING.Alpha}")
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING_Beta: {SCF.MIXING.Beta}")
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING_Nbroyden: {SCF.MIXING.Nbroyden}")
    return