from pycp2k.inputsection import InputSection


class _gga_x_pw918(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._f = None
        self._alpha = None
        self._expo = None
        self._name = "GGA_X_PW91"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_f': '_F', '_alpha': '_ALPHA', '_expo': '_EXPO'}
        self._attributes = ['Section_parameters']

