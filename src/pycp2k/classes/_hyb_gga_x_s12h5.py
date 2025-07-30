from pycp2k.inputsection import InputSection


class _hyb_gga_x_s12h5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._e = None
        self._alpha = None
        self._name = "HYB_GGA_X_S12H"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_e': '_E', '_alpha': '_ALPHA'}
        self._attributes = ['Section_parameters']

