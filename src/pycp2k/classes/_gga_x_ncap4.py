from pycp2k.inputsection import InputSection


class _gga_x_ncap4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._alpha = None
        self._beta = None
        self._mu = None
        self._zeta = None
        self._name = "GGA_X_NCAP"
        self._keywords = {'Scale': 'SCALE', '_alpha': '_ALPHA', '_beta': '_BETA', '_mu': '_MU', '_zeta': '_ZETA'}
        self._attributes = ['Section_parameters']

