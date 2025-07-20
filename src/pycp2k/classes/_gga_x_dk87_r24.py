from pycp2k.inputsection import InputSection


class _gga_x_dk87_r24(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a1 = None
        self._b1 = None
        self._alpha = None
        self._name = "GGA_X_DK87_R2"
        self._keywords = {'Scale': 'SCALE', '_a1': '_A1', '_b1': '_B1', '_alpha': '_ALPHA'}
        self._attributes = ['Section_parameters']

