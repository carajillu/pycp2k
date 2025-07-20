from pycp2k.inputsection import InputSection
from ._polar_matrix2 import _polar_matrix2


class _print87(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.POLAR_MATRIX = _polar_matrix2()
        self._name = "PRINT"
        self._subsections = {'POLAR_MATRIX': 'POLAR_MATRIX'}

