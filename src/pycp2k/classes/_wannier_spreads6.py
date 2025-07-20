from pycp2k.inputsection import InputSection
from ._each228 import _each228


class _wannier_spreads6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Second_moments = None
        self.Periodic = None
        self.EACH = _each228()
        self._name = "WANNIER_SPREADS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Second_moments': 'SECOND_MOMENTS', 'Periodic': 'PERIODIC'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

