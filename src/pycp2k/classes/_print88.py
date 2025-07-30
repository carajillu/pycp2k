from pycp2k.inputsection import InputSection
from ._apt1 import _apt1


class _print88(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.APT = _apt1()
        self._name = "PRINT"
        self._subsections = {'APT': 'APT'}

