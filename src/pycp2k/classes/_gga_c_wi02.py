from pycp2k.inputsection import InputSection


class _gga_c_wi02(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._k = None
        self._name = "GGA_C_WI0"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_k': '_K'}
        self._attributes = ['Section_parameters']

