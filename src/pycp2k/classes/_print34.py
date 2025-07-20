from pycp2k.inputsection import InputSection
from ._program_run_info18 import _program_run_info18
from ._wannier_cubes4 import _wannier_cubes4
from ._wannier_centers4 import _wannier_centers4
from ._wannier_spreads4 import _wannier_spreads4
from ._loc_restart4 import _loc_restart4
from ._total_dipole4 import _total_dipole4
from ._molecular_dipoles4 import _molecular_dipoles4
from ._molecular_moments4 import _molecular_moments4
from ._molecular_states4 import _molecular_states4
from ._wannier_states4 import _wannier_states4


class _print34(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info18()
        self.WANNIER_CUBES = _wannier_cubes4()
        self.WANNIER_CENTERS = _wannier_centers4()
        self.WANNIER_SPREADS = _wannier_spreads4()
        self.LOC_RESTART = _loc_restart4()
        self.TOTAL_DIPOLE = _total_dipole4()
        self.MOLECULAR_DIPOLES = _molecular_dipoles4()
        self.MOLECULAR_MOMENTS = _molecular_moments4()
        self.MOLECULAR_STATES = _molecular_states4()
        self.WANNIER_STATES = _wannier_states4()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

