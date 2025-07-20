from pycp2k.inputsection import InputSection


class _hyb_gga_xc_lc_qtp4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._alpha = None
        self._beta = None
        self._omega = None
        self._ac = None
        self._name = "HYB_GGA_XC_LC_QTP"
        self._keywords = {'Scale': 'SCALE', '_alpha': '_ALPHA', '_beta': '_BETA', '_omega': '_OMEGA', '_ac': '_AC'}
        self._attributes = ['Section_parameters']

