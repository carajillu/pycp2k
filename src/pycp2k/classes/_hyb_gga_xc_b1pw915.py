from pycp2k.inputsection import InputSection


class _hyb_gga_xc_b1pw915(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cx = None
        self._name = "HYB_GGA_XC_B1PW91"
        self._keywords = {'Scale': 'SCALE', '_cx': '_CX'}
        self._attributes = ['Section_parameters']

