from pycp2k.inputsection import InputSection
from ._each372 import _each372


class _voronoi2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Append = None
        self.Sanity_check = None
        self.Overwrite = None
        self.Skip_first = None
        self.Verbose = None
        self.Output_emp = None
        self.Output_text = None
        self.Refinement_factor = None
        self.Voronoi_radii = None
        self.User_radii = None
        self.EACH = _each372()
        self._name = "VORONOI"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Append': 'APPEND', 'Sanity_check': 'SANITY_CHECK', 'Overwrite': 'OVERWRITE', 'Skip_first': 'SKIP_FIRST', 'Verbose': 'VERBOSE', 'Output_emp': 'OUTPUT_EMP', 'Output_text': 'OUTPUT_TEXT', 'Refinement_factor': 'REFINEMENT_FACTOR', 'Voronoi_radii': 'VORONOI_RADII', 'User_radii': 'USER_RADII'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

