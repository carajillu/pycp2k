from pycp2k.inputsection import InputSection
from ._point57 import _point57


class _gyration_radius4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = []
        self.Points = self.Atoms
        self.Kinds = []
        self.POINT_list = []
        self._name = "GYRATION_RADIUS"
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Kinds': 'KINDS'}
        self._repeated_subsections = {'POINT': '_point57'}
        self._repeated_aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point57()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

