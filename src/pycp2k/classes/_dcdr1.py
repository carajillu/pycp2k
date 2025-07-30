from pycp2k.inputsection import InputSection
from ._print88 import _print88
from ._interpolator14 import _interpolator14


class _dcdr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.List_of_atoms = []
        self.Distributed_origin = None
        self.Orbital_center = None
        self.Reference = None
        self.Reference_point = None
        self.PRINT = _print88()
        self.INTERPOLATOR = _interpolator14()
        self._name = "DCDR"
        self._keywords = {'Distributed_origin': 'DISTRIBUTED_ORIGIN', 'Orbital_center': 'ORBITAL_CENTER', 'Reference': 'REFERENCE', 'Reference_point': 'REFERENCE_POINT'}
        self._repeated_keywords = {'List_of_atoms': 'LIST_OF_ATOMS'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._aliases = {'Do_gauge': 'Distributed_origin'}
        self._attributes = ['Section_parameters']


    @property
    def Do_gauge(self):
        """
        See documentation for Distributed_origin
        """
        return self.Distributed_origin

    @Do_gauge.setter
    def Do_gauge(self, value):
        self.Distributed_origin = value
