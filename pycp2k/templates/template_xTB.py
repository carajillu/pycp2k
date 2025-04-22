from pycp2k import CP2K
import os
class TemplatexTB(CP2K):
    template="""
    &FORCE_EVAL
      METHOD QS
      &DFT
        &QS
         METHOD XTB
         # PyCP2K does not support XTB as a section, so we leave this out for now
         #&XTB
         #   CHECK_ATOMIC_CHARGES T    ! Keyword to check if Mulliken charges are physically reasonable
         #   DO_EWALD  T               ! Ewald summation is required for periodic structures
         #   USE_HALOGEN_CORRECTION T  ! Element-specific correction for halogen interactions (Cl, Br) with (O, N)
         #&END XTB
        &END QS
      &END DFT
    &END FORCE_EVAL
    """

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_xTB.in"
            with open(template_filein,"w") as f:
                f.write(self.template)
        self.parse(template_filein)
        os.remove("template_xTB.in")
        
    def assign_section(self,calc:CP2K,**kwargs):
         if "feval_list_idx" not in kwargs.keys():
            print("feval_list_idx not supplied. Setting to 0.")
            feval_list_idx=0
         else:
            feval_list_idx=kwargs["feval_list_id"]
        
         calc_FORCE_EVAL_list=calc.CP2K_INPUT.FORCE_EVAL_list
         if (len(calc_FORCE_EVAL_list)==0):
            calc.CP2K_INPUT.FORCE_EVAL_add()
         
         calc.CP2K_INPUT.FORCE_EVAL_list[feval_list_idx].DFT.QS.METHOD=self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.QS.METHOD
         #TODO Add functionality for the &XTB section, when (if?) pyCP2K supports it
         

        
         