from pycp2k.inputsection import InputSection


class _hyb_gga_xc_o3lyp7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._clyp = None
        self._name = "HYB_GGA_XC_O3LYP"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_clyp': '_CLYP'}
        self._attributes = ['Section_parameters']

