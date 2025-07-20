from pycp2k.inputsection import InputSection


class _hyb_gga_xc_lc_blyp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._omega = None
        self._name = "HYB_GGA_XC_LC_BLYP"
        self._keywords = {'Scale': 'SCALE', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

