from pycp2k.inputsection import InputSection


class _hyb_gga_xc_x3lyp5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._ax = None
        self._ac = None
        self._ax1 = None
        self._ax2 = None
        self._name = "HYB_GGA_XC_X3LYP"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_ax': '_AX', '_ac': '_AC', '_ax1': '_AX1', '_ax2': '_AX2'}
        self._attributes = ['Section_parameters']

