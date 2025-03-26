from pycp2k import CP2K
import os
class TemplateSmearing(CP2K):
    template="""
    &FORCE_EVAL
       &DFT
         &SCF
           &MIXING
              METHOD BROYDEN_MIXING
              BETA 1.0
              ALPHA 0.6
              NBUFFER 15
           &END MIXING
           &SMEAR
              METHOD FERMI_DIRAC
              ELECTRONIC_TEMPERATURE 500
           &END SMEAR
         &END SCF
       &END DFT
    &END FORCE_EVAL
    """

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_smear.in"
            with open(template_filein,"w") as f:
                f.write(self.template)
        self.parse(template_filein)
        os.remove("template_smear.in")
        
    def assign_section(self,calc:CP2K,**kwargs):
        if "feval_list_idx" not in kwargs.keys():
            print("feval_list_idx not supplied. Setting to 0.")
            feval_list_idx=0
        else:
            feval_list_idx=kwargs["feval_list_id"]
        
        calc_FORCE_EVAL_list=calc.CP2K_INPUT.FORCE_EVAL_list
        if (len(calc_FORCE_EVAL_list)==0):
            calc.CP2K_INPUT.FORCE_EVAL_add()

        MIXING_METHOD=self.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.SCF.MIXING.Method
        MIXING_ALPHA=self.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.SCF.MIXING.Alpha
        MIXING_BETA=self.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.SCF.MIXING.Beta

        SMEAR_METHOD=self.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.SCF.SMEAR.Method
        SMEAR_TEMPERATURE=self.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.SCF.SMEAR.Electronic_temperature

        