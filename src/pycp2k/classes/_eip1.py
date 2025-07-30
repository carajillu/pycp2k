from pycp2k.inputsection import InputSection
from ._print68 import _print68


class _eip1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eip_model = None
        self.Eip_model = None
        self.PRINT = _print68()
        self._name = "EIP"
        self._keywords = {'Eip_model': 'EIP-MODEL'}
        self._subsections = {'PRINT': 'PRINT'}

