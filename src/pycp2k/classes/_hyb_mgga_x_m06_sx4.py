from pycp2k.inputsection import InputSection


class _hyb_mgga_x_m06_sx4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._a1 = None
        self._a2 = None
        self._a3 = None
        self._a4 = None
        self._a5 = None
        self._a6 = None
        self._a7 = None
        self._a8 = None
        self._a9 = None
        self._a10 = None
        self._a11 = None
        self._b0 = None
        self._b1 = None
        self._b2 = None
        self.B3 = None
        self._b4 = None
        self._b5 = None
        self._beta = None
        self._omega = None
        self._name = "HYB_MGGA_X_M06_SX"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_a1': '_A1', '_a2': '_A2', '_a3': '_A3', '_a4': '_A4', '_a5': '_A5', '_a6': '_A6', '_a7': '_A7', '_a8': '_A8', '_a9': '_A9', '_a10': '_A10', '_a11': '_A11', '_b0': '_B0', '_b1': '_B1', '_b2': '_B2', 'B3': 'B3', '_b4': '_B4', '_b5': '_B5', '_beta': '_BETA', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

