from pycp2k.inputsection import InputSection
from ._program_run_info49 import _program_run_info49
from ._wannier_cubes15 import _wannier_cubes15
from ._wannier_centers15 import _wannier_centers15
from ._wannier_spreads15 import _wannier_spreads15
from ._loc_restart15 import _loc_restart15
from ._total_dipole14 import _total_dipole14
from ._molecular_dipoles14 import _molecular_dipoles14
from ._molecular_moments14 import _molecular_moments14
from ._molecular_states14 import _molecular_states14
from ._wannier_states14 import _wannier_states14


class _print83(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info49()
        self.WANNIER_CUBES = _wannier_cubes15()
        self.WANNIER_CENTERS = _wannier_centers15()
        self.WANNIER_SPREADS = _wannier_spreads15()
        self.LOC_RESTART = _loc_restart15()
        self.TOTAL_DIPOLE = _total_dipole14()
        self.MOLECULAR_DIPOLES = _molecular_dipoles14()
        self.MOLECULAR_MOMENTS = _molecular_moments14()
        self.MOLECULAR_STATES = _molecular_states14()
        self.WANNIER_STATES = _wannier_states14()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

