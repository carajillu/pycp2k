from pycp2k import CP2K
import os
class CP2K(CP2K):

    def __init__(self,project_name:str="TEMPLATE",print_level:str="MEDIUM",run_type:str="ENERGY",\
                 working_directory:str=os.getcwd(),cp2k_command:str="cp2k.psmp"):
        super().__init__()
        self.working_directory=working_directory
        self.project_name=project_name
        self.cp2k_command=cp2k_command
        self.CP2K_INPUT.GLOBAL.Project_name=project_name
        self.CP2K_INPUT.GLOBAL.Print_level=print_level
        self.CP2K_INPUT.GLOBAL.Run_type=run_type
        print(f"CP2K_command: {self.cp2k_command}")
        print(f"Working directory: {self.working_directory}")
        print(f"CP2K_INPUT.GLOBAL.Project_name: {self.CP2K_INPUT.GLOBAL.Project_name}")
        print(f"CP2K_INPUT.GLOBAL.Print_level: {self.CP2K_INPUT.GLOBAL.Print_level}")
        print(f"CP2K_INPUT.GLOBAL.Run_type: {self.CP2K_INPUT.GLOBAL.Run_type}")
