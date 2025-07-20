from pycp2k.inputsection import InputSection
from ._rng_init9 import _rng_init9
from ._extra_dof1 import _extra_dof1


class _piglet1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nextra_dof = None
        self.Matrices_file_name = None
        self.Smatrix_init = None
        self.Thermostat_energy = None
        self.RNG_INIT = _rng_init9()
        self.EXTRA_DOF = _extra_dof1()
        self._name = "PIGLET"
        self._keywords = {'Nextra_dof': 'NEXTRA_DOF', 'Matrices_file_name': 'MATRICES_FILE_NAME', 'Smatrix_init': 'SMATRIX_INIT', 'Thermostat_energy': 'THERMOSTAT_ENERGY'}
        self._subsections = {'RNG_INIT': 'RNG_INIT', 'EXTRA_DOF': 'EXTRA_DOF'}

