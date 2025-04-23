from io import StringIO, BytesIO
from ase.io import read,write
from ase import Atoms
from pycp2k import CP2K
import os
from pycp2k.workflows.singlepoint_castep import add_atoms, add_kinds
import argparse

cp2k_input="""
&GLOBAL
  PROJECT_NAME xtb_test
  RUN_TYPE ENERGY
&END GLOBAL
&FORCE_EVAL
  #&PROPERTIES
    #&TDDFPT
    #   NSTATES 5
    #   KERNEL STDA
    #   &DIPOLE_MOMENTS
    #      DIPOLE_FORM LENGTH
    #   &END
       #&STDA 
       #   FRACTION 0.5
       #   DO_EWALD F
       #&END STDA
    #&END
  #&END
  &DFT
    &SCF
      MAX_SCF 30
      EPS_SCF 1e-07
      SCF_GUESS ATOMIC
      &OT ON
        PRECONDITIONER FULL_SINGLE_INVERSE
      &END OT
    &END SCF
    &QS
      EPS_DEFAULT 1e-12
      METHOD XTB
      #&XTB
      #  DO_EWALD FALSE
      #&END XTB
    &END QS
  &END DFT
  &SUBSYS
    &CELL
      A 10.0 0.0 0.0
      B 0.0 10.0 0.0
      C 0.0 0.0 10.0
      PERIODIC XYZ
    &END CELL
    &COORD
      O 0.0 0.0 0.119262
      H 0.0 0.763239 -0.477047
      H 0.0 -0.763239 -0.477047
    &END COORD
  &END SUBSYS
&END FORCE_EVAL
"""

def parse():
    parser = argparse.ArgumentParser(description='Singlepoint calculation from castep cell')
    parser.add_argument("--cp2k_command", type=str, default=None, help="CP2K command")
    parser.add_argument("--input_cp2k", type=str, default=None, help="CP2K input file")
    parser.add_argument("--input_xyz", type=str, default=None, help="Input structure")
    parser.add_argument("--multiplicity", type=int, default=1, help="Multiplicity")
    parser.add_argument("--charge", type=int, default=1, help="Charge")
    parser.add_argument("--geo_opt",action="store_true",help="Run geometry optimization")
    return parser.parse_args()
    

def build_calc(cp2k_input_file: str=None, cp2k_command: str=None):
    calc=CP2K()
    if cp2k_command is None:
        cp2k_command="cp2k.psmp"
    calc.cp2k_command=cp2k_command

    if cp2k_input_file is None:
       with open("cp2k_input.in","w") as f:
           f.write(cp2k_input)
       cp2k_input_file="cp2k_input.in"
    calc.parse(cp2k_input_file)
    os.remove("cp2k_input.in")
    calc.project_name=calc.CP2K_INPUT.GLOBAL.Project_name
    calc.working_directory=os.getcwd()
    
    return calc

def add_subsys(calc: CP2K, atoms: Atoms):
    add_atoms(calc, atoms)
    #add_kinds(calc,atoms) #Doesn't work yet if kinds are not already in the input file
    return

def add_geopt():
    raise NotImplemented
    return

if __name__=="__main__":
    args=parse()
    calc=build_calc(args.input_cp2k,args.cp2k_command)
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Multiplicity=args.multiplicity

    z=read(args.input_xyz)
    add_subsys(calc,z)

    calc.run()
