from pycp2k.inputsection import InputSection
from ._point13 import _point13


class _xyz_outerdiag1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Component_a = None
        self.Component_b = None
        self.Pbc = None
        self.POINT_list = []
        self._name = "XYZ_OUTERDIAG"
        self._keywords = {'Atoms': 'ATOMS', 'Component_a': 'COMPONENT_A', 'Pbc': 'PBC', 'Component_b': 'COMPONENT_B'}
        self._repeated_subsections = {'POINT': '_point13'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point13()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Points(self):
        """
        See documentation for Atoms
        """
        return self.Atoms

    @Points.setter
    def Points(self, value):
        self.Atoms = value
