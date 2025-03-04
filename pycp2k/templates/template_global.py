from pycp2k import CP2K
class TemplateGlobal(CP2K):
    print_levels = {"SILENT","LOW", "MEDIUM", "HIGH", "DEBUG"}
    def __init__(self,template_filein):
        super().__init__()
        self.parse(template_filein)
        if self.CP2K_INPUT.GLOBAL.Print_level not in self.print_levels:
           raise ValueError(f"Invalid print level: {self.CP2K_INPUT.GLOBAL.Print_level}")
        
    def set_print_level(self, calc: CP2K):
        if hasattr(self, "CP2K_INPUT") and hasattr(self.CP2K_INPUT, "GLOBAL"):
           calc.CP2K_INPUT.GLOBAL.Print_level = self.CP2K_INPUT.GLOBAL.Print_level
        else:
           print("TemplateGlobal object has no PRINT_LEVEL value set. Setting PRINT_LEVEL to MEDIUM as CP2K default")
           calc.CP2K_INPUT.GLOBAL.Print_level="MEDIUM"
    
    def set_project_name(self, calc: CP2K):
        calc.CP2K_INPUT.GLOBAL.Project_name=self.calc.CP2K_INPUT.GLOBAL.Project_name