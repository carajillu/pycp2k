from pycp2k.inputsection import InputSection
from ._program_run_info48 import _program_run_info48
from ._wannier_cubes14 import _wannier_cubes14
from ._wannier_centers14 import _wannier_centers14
from ._wannier_spreads14 import _wannier_spreads14
from ._loc_restart14 import _loc_restart14
from ._total_dipole13 import _total_dipole13
from ._molecular_dipoles13 import _molecular_dipoles13
from ._molecular_moments13 import _molecular_moments13
from ._molecular_states13 import _molecular_states13
from ._wannier_states13 import _wannier_states13


class _print81(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info48()
        self.WANNIER_CUBES = _wannier_cubes14()
        self.WANNIER_CENTERS = _wannier_centers14()
        self.WANNIER_SPREADS = _wannier_spreads14()
        self.LOC_RESTART = _loc_restart14()
        self.TOTAL_DIPOLE = _total_dipole13()
        self.MOLECULAR_DIPOLES = _molecular_dipoles13()
        self.MOLECULAR_MOMENTS = _molecular_moments13()
        self.MOLECULAR_STATES = _molecular_states13()
        self.WANNIER_STATES = _wannier_states13()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

