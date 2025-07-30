from pycp2k.inputsection import InputSection
from ._program_run_info34 import _program_run_info34
from ._wannier_cubes12 import _wannier_cubes12
from ._wannier_centers12 import _wannier_centers12
from ._wannier_spreads12 import _wannier_spreads12
from ._loc_restart12 import _loc_restart12
from ._total_dipole11 import _total_dipole11
from ._molecular_dipoles11 import _molecular_dipoles11
from ._molecular_moments11 import _molecular_moments11
from ._molecular_states11 import _molecular_states11
from ._wannier_states11 import _wannier_states11


class _print59(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info34()
        self.WANNIER_CUBES = _wannier_cubes12()
        self.WANNIER_CENTERS = _wannier_centers12()
        self.WANNIER_SPREADS = _wannier_spreads12()
        self.LOC_RESTART = _loc_restart12()
        self.TOTAL_DIPOLE = _total_dipole11()
        self.MOLECULAR_DIPOLES = _molecular_dipoles11()
        self.MOLECULAR_MOMENTS = _molecular_moments11()
        self.MOLECULAR_STATES = _molecular_states11()
        self.WANNIER_STATES = _wannier_states11()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

