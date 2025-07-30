from pycp2k.inputsection import InputSection
from ._program_run_info55 import _program_run_info55
from ._coord_fit_points1 import _coord_fit_points1
from ._resp_charges_to_file1 import _resp_charges_to_file1
from ._v_resp_cube1 import _v_resp_cube1


class _print92(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info55()
        self.COORD_FIT_POINTS = _coord_fit_points1()
        self.RESP_CHARGES_TO_FILE = _resp_charges_to_file1()
        self.V_RESP_CUBE = _v_resp_cube1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'COORD_FIT_POINTS': 'COORD_FIT_POINTS', 'RESP_CHARGES_TO_FILE': 'RESP_CHARGES_TO_FILE', 'V_RESP_CUBE': 'V_RESP_CUBE'}

