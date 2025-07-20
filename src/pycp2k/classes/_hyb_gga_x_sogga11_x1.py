from pycp2k.inputsection import InputSection


class _hyb_gga_x_sogga11_x1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._mu = None
        self._a0 = None
        self._a1 = None
        self._a2 = None
        self._a3 = None
        self._a4 = None
        self._a5 = None
        self._b0 = None
        self._b1 = None
        self._b2 = None
        self._b3 = None
        self._b4 = None
        self._b5 = None
        self._cx = None
        self._name = "HYB_GGA_X_SOGGA11_X"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_mu': '_MU', '_a0': '_A0', '_a1': '_A1', '_a2': '_A2', '_a3': '_A3', '_a4': '_A4', '_a5': '_A5', '_b0': '_B0', '_b1': '_B1', '_b2': '_B2', '_b3': '_B3', '_b4': '_B4', '_b5': '_B5', '_cx': '_CX'}
        self._attributes = ['Section_parameters']

