from pycp2k.inputsection import InputSection


class _hyb_gga_xc_b3lyp_mcm26(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._p1 = None
        self._p2 = None
        self._p3 = None
        self._p4 = None
        self._p5 = None
        self._p6 = None
        self._name = "HYB_GGA_XC_B3LYP_MCM2"
        self._keywords = {'Scale': 'SCALE', '_p1': '_P1', '_p2': '_P2', '_p3': '_P3', '_p4': '_P4', '_p5': '_P5', '_p6': '_P6'}
        self._attributes = ['Section_parameters']

