from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_SCF_OT(calc:CP2K,**kwargs):
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
    #inner scf loop
    SCF.Scf_guess=kwargs.get("scf_guess","RESTART")
    SCF.Max_scf=kwargs.get("max_scf",20)
    SCF.Eps_scf=kwargs.get("eps_scf",1e-6)
    print(f"scf_guess = {SCF.Scf_guess}")
    print(f"max_scf = {SCF.Max_scf}")
    print(f"eps_scf = {SCF.Eps_scf}")

    #outer scf loop
    SCF.OUTER_SCF.Max_scf=kwargs.get("outer_max_scf",2)
    SCF.OUTER_SCF.Eps_scf=kwargs.get("outer_eps_scf",1e-6)
    print(f"outer_max_scf = {SCF.OUTER_SCF.Max_scf}")
    print(f"outer_eps_scf = {SCF.OUTER_SCF.Eps_scf}")