from pycp2k.inputsection import InputSection


class _gga_x_pw91_mod8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._bt = None
        self._alpha = None
        self._expo = None
        self._name = "GGA_X_PW91_MOD"
        self._keywords = {'Scale': 'SCALE', '_bt': '_BT', '_alpha': '_ALPHA', '_expo': '_EXPO'}
        self._attributes = ['Section_parameters']

