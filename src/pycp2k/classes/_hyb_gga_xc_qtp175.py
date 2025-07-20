from pycp2k.inputsection import InputSection


class _hyb_gga_xc_qtp175(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._ac = None
        self._name = "HYB_GGA_XC_QTP17"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_ac': '_AC'}
        self._attributes = ['Section_parameters']

