from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_smear(calc:CP2K,**kwargs):
    raise NotImplementedError("Smearing is not implemented yet.")
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF
    SCF.Smear.Method=kwargs.get("method","FERMI_DIRAC")
    SCF.Smear.Width=kwargs.get("width",0.01)
    return
