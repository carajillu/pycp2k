from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_xTB(calc:CP2K,**kwargs):
    feval_idx=kwargs.get("feval_idx",0)
    if not calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx]:
        raise ValueError(f"FORCE_EVAL section {feval_idx} not found in calculator")

    print(f"===Adding xTB to FORCE_EVAL section {feval_idx}===")
    calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx].Method="QS"
    DFT=calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx].DFT
    DFT.QS.Method="XTB"
    DFT.QS.XTB.Check_atomic_charges=kwargs.get("check_atomic_charges",False)
    DFT.QS.XTB.Do_ewald=kwargs.get("do_ewald",True)  
    DFT.QS.XTB.Use_halogen_correction=kwargs.get("use_halogen_correction",True)
    print(f"check_atomic_charges = {DFT.QS.XTB.Check_atomic_charges}")
    print(f"do_ewald = {DFT.QS.XTB.Do_ewald}")
    print(f"use_halogen_correction = {DFT.QS.XTB.Use_halogen_correction}")
    return
