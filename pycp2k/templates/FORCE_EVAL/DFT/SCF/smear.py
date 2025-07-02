from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_smear(calc:CP2K,**kwargs):
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF
    SCF.Added_mos=kwargs.get("SCF_Added_mos","10 10")
    SCF.SMEAR.Method=kwargs.get("SMEAR_Method","FERMI_DIRAC")
    SCF.SMEAR.Electronic_temperature=kwargs.get("SMEAR_Electronic_temperature",300.0)
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.SMEAR.Method: {SCF.SMEAR.Method}")
    print(f"CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.SMEAR.Electronic_temperature: {SCF.SMEAR.Electronic_temperature}")
    return
