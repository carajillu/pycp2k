from pycp2k.inputsection import InputSection


class _hyb_gga_xc_mb3lyp_rc046(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._ax = None
        self._ac = None
        self._d = None
        self._name = "HYB_GGA_XC_MB3LYP_RC04"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_ax': '_AX', '_ac': '_AC', '_d': '_D'}
        self._attributes = ['Section_parameters']

