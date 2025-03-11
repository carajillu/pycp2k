from pycp2k import CP2K
import os
class TemplateGeoOpt(CP2K):
    template="""&MOTION
                    &GEO_OPT
                       MINIMIZER LBFGS
                    &END
                &END

                &GLOBAL
                    RUN_TYPE GEO_OPT
                &END"""

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_geopt.in"
            with open(template_filein,"w") as f:
                f.write(self.template)
        self.parse(template_filein)
        os.remove("template_geopt.in")

        
    def assign_section(self,calc:CP2K):
        #Assign run type
        RUN_TYPE=self.CP2K_INPUT.GLOBAL.Run_type
        calc.CP2K_INPUT.GLOBAL.Run_type=RUN_TYPE

        #Assign Minimizer for Geo_opt
        MINIMIZER=self.CP2K_INPUT.MOTION.GEO_OPT.Minimizer
        calc.CP2K_INPUT.MOTION.GEO_OPT.Minimizer=MINIMIZER
        
    