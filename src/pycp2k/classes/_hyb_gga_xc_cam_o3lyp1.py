from pycp2k.inputsection import InputSection


class _hyb_gga_xc_cam_o3lyp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._csr = None
        self._b = None
        self._c = None
        self._clyp = None
        self._clr = None
        self._omega = None
        self._name = "HYB_GGA_XC_CAM_O3LYP"
        self._keywords = {'Scale': 'SCALE', '_csr': '_CSR', '_b': '_B', '_c': '_C', '_clyp': '_CLYP', '_clr': '_CLR', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

