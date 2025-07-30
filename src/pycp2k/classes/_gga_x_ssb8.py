from pycp2k.inputsection import InputSection


class _gga_x_ssb8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._e = None
        self._f = None
        self._u = None
        self._delta = None
        self._name = "GGA_X_SSB"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_e': '_E', '_f': '_F', '_u': '_U', '_delta': '_DELTA'}
        self._attributes = ['Section_parameters']

