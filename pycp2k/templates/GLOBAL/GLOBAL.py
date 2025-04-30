from pycp2k import CP2K
import os
class CP2K(CP2K):

    def __init__(self,project_name:str="TEMPLATE",print_level:str="MEDIUM",run_type:str="ENERGY"):
        super().__init__()
        self.CP2K_INPUT.GLOBAL.Project_name=project_name
        self.CP2K_INPUT.GLOBAL.Print_level=print_level
        self.CP2K_INPUT.GLOBAL.Run_type=run_type
        print(f"CP2K_INPUT.GLOBAL.Project_name: {self.CP2K_INPUT.GLOBAL.Project_name}")
        print(f"CP2K_INPUT.GLOBAL.Print_level: {self.CP2K_INPUT.GLOBAL.Print_level}")
        print(f"CP2K_INPUT.GLOBAL.Run_type: {self.CP2K_INPUT.GLOBAL.Run_type}")
