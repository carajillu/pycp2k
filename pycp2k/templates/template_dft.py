from pycp2k import CP2K
import os
class TemplateDFT(CP2K):
    template="""
    &FORCE_EVAL
       &DFT
         &SCF
           EPS_SCF 1.0E-6
           &OT
             PRECONDITIONER FULL_ALL
             MINIMIZER DIIS
           &END OT
         &END SCF
       &END DFT
    &END FORCE_EVAL
    """

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_dft.in"
            with open(template_filein,"w") as f:
                f.write(self.template)
        self.parse(template_filein)
        os.remove("template_dft.in")
        
    def assign_section(self,calc:CP2K,**kwargs):
        if "feval_list_idx" not in kwargs.keys():
            print("feval_list_idx not supplied. Setting to 0.")
            kwargs["feval_list_idx"]=0
        
        calc_FORCE_EVAL_list=calc.CP2K_INPUT.FORCE_EVAL_list
        if (len(calc_FORCE_EVAL_list)==0):
            calc.CP2K_INPUT.FORCE_EVAL_add()

        EPS_SCF=self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Eps_scf
        calc.CP2K_INPUT.FORCE_EVAL_list[kwargs["feval_list_idx"]].DFT.SCF.Eps_scf=EPS_SCF

        PRECONDITIONER=self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.OT.Preconditioner
        calc.CP2K_INPUT.FORCE_EVAL_list[kwargs["feval_list_idx"]].DFT.SCF.OT.Preconditioner=PRECONDITIONER

        MINIMIZER=self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.OT.Minimizer
        calc.CP2K_INPUT.FORCE_EVAL_list[kwargs["feval_list_idx"]].DFT.SCF.OT.Minimizer=MINIMIZER