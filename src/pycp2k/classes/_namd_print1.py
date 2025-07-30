from pycp2k.inputsection import InputSection
from ._each603 import _each603


class _namd_print1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Print_virtuals = None
        self.EACH = _each603()
        self._name = "NAMD_PRINT"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Print_virtuals': 'PRINT_VIRTUALS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

