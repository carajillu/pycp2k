from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_OT(calc:CP2K,**kwargs):
    #Ads the SCF section to a calculator containing a DFT section
    feval_idx=kwargs.get("feval_idx",0)
    if not calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx]:
        print(f"FORCE_EVAL section {feval_idx} not found in calculator, creating new one.")
        calc.CP2K_INPUT.FORCE_EVAL_add()
    
    print(f"===Adding SCF-OT section to FORCE_EVAL section {feval_idx}===")
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx].DFT.SCF 
    #preconditioner
    SCF.OT.Preconditioner=kwargs.get("preconditioner","FULL_ALL")
    SCF.OT.Minimizer=kwargs.get("minimizer","DIIS")
    print(f"preconditioner = {SCF.OT.Preconditioner}")
    print(f"minimizer = {SCF.OT.Minimizer}")

def del_OT(calc:CP2K):
    del(calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.OT)
    del(calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF._subsections['OT'])
    return