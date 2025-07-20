from pycp2k.inputsection import InputSection


class _gga_c_lypr6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._m1 = None
        self._m2 = None
        self._omega = None
        self._name = "GGA_C_LYPR"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_m1': '_M1', '_m2': '_M2', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

