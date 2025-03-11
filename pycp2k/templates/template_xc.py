from pycp2k import CP2K
import os
class TemplateXC(CP2K):
    template="""
    &FORCE_EVAL
       &DFT
         &XC
           &XC_FUNCTIONAL PBE
           &END XC_FUNCTIONAL
         &END XC
       &END DFT
    &END FORCE_EVAL
    """

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_xc.in"
            with open(template_filein,"w") as f:
                f.write(self.template)
        self.parse(template_filein)
        os.remove("template_xc.in")
        
    def assign_section(self,calc:CP2K,**kwargs):
        if "feval_list_idx" not in kwargs.keys():
            print("feval_list_idx not supplied. Setting to 0.")
            kwargs["feval_list_idx"]=0
        
        calc_FORCE_EVAL_list=calc.CP2K_INPUT.FORCE_EVAL_list
        if (len(calc_FORCE_EVAL_list)==0):
            calc.CP2K_INPUT.FORCE_EVAL_add()

        PBE=self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL
        calc.CP2K_INPUT.FORCE_EVAL_list[kwargs["feval_list_idx"]].DFT.XC.XC_FUNCTIONAL.PBE=PBE
    