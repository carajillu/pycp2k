from pycp2k import CP2K
import os
class TemplateGlobal(CP2K):
    template="""&GLOBAL
                   PROJECT_NAME TEMPLATE
                   PRINT_LEVEL MEDIUM
                &END GLOBAL"""
    print_levels = {"SILENT","LOW", "MEDIUM", "HIGH", "DEBUG"}

    def __init__(self,template_filein:str=None):
        super().__init__()

        if template_filein is None:
            template_filein="template_global.in"
            with open(template_filein,"w") as f:
                f.write(template)
        self.parse(template_filein)
        os.remove("template_global.in")

        if self.CP2K_INPUT.GLOBAL.Print_level not in self.print_levels:
           raise ValueError(f"Invalid print level: {self.CP2K_INPUT.GLOBAL.Print_level}")
        
    def assign_section(self,calc:CP2K):
        GLOBAL=self.CP2K_INPUT.GLOBAL
        calc.CP2K_INPUT.GLOBAL=GLOBAL
        
    