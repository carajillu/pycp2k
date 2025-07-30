from pycp2k.inputsection import InputSection


class _gga_c_chachiyo2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._ap = None
        self._bp = None
        self._af = None
        self._bf = None
        self._h = None
        self._name = "GGA_C_CHACHIYO"
        self._keywords = {'Scale': 'SCALE', '_ap': '_AP', '_bp': '_BP', '_af': '_AF', '_bf': '_BF', '_h': '_H'}
        self._attributes = ['Section_parameters']

