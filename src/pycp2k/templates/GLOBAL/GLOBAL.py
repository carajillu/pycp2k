import os
import pycp2k
from pycp2k import CP2K
from pycp2k.templates.FORCE_EVAL.SUBSYS.add_atoms import add_coords, add_cell
from pycp2k.templates.FORCE_EVAL.SUBSYS.add_kinds import add_kinds
class CP2K(CP2K):

    def __init__(self,project_name:str="TEMPLATE",print_level:str="MEDIUM",run_type:str="ENERGY",\
                 working_directory:str=None,cp2k_command:str="cp2k.psmp"):
        super().__init__()
        self._atoms=None
        self.working_directory=working_directory
        self.project_name=project_name
        self.cp2k_command=cp2k_command
        self.CP2K_INPUT.GLOBAL.Project_name=project_name
        self.CP2K_INPUT.GLOBAL.Print_level=print_level
        self.CP2K_INPUT.GLOBAL.Run_type=run_type
        self.version=float(pycp2k.config.build_version)
        self.revision=pycp2k.config.build_revision
        self.working_directory=working_directory
        print(f"CP2K version: {self.version}")
        print(f"CP2K revision: {self.revision}")
        print(f"CP2K_command: {self.cp2k_command}")
        print(f"Working directory: {self.working_directory}")
        print(f"CP2K_INPUT.GLOBAL.Project_name: {self.CP2K_INPUT.GLOBAL.Project_name}")
        print(f"CP2K_INPUT.GLOBAL.Print_level: {self.CP2K_INPUT.GLOBAL.Print_level}")
        print(f"CP2K_INPUT.GLOBAL.Run_type: {self.CP2K_INPUT.GLOBAL.Run_type}")
    
    @property
    def atoms(self):
        return self._atoms
    @atoms.setter
    def atoms(self,atoms):
        self._atoms=atoms
        if len(self.CP2K_INPUT.FORCE_EVAL_list)==0:
           self.CP2K_INPUT.FORCE_EVAL_add()
        add_coords(atoms,self)
        add_cell(atoms,self)
        add_kinds(atoms,self)

    @property
    def working_directory(self):
        return self._working_directory
    @working_directory.setter
    def working_directory(self,working_directory):
        if working_directory is None:
           self._working_directory=os.getcwd()
        else:
           os.makedirs(working_directory,exist_ok=True)
           self._working_directory=os.path.abspath(working_directory)


    def cleanup(self,quiet:bool=False):
        
        if not quiet:
           z=""
           while (z.upper()) not in ["Y","N"]:
               z=input(f"WARNING: You are about to run 'rm -rf {self.project_name}*'. \
                       Check that you are not removing files you want to keep. Do you wish to continue?[Y/N]\n")
           if z.upper()=="N":
               print("Aborting cleanup")
               return
        cmd=f"rm -rf {self.project_name}*"
        os.system(cmd)
        return
               
