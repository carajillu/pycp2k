from pycp2k.inputsection import InputSection
from ._each89 import _each89


class _force_mixing_labels1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Format = None
        self.Print_atom_kind = None
        self.EACH = _each89()
        self._name = "FORCE_MIXING_LABELS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Format': 'FORMAT', 'Print_atom_kind': 'PRINT_ATOM_KIND'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

