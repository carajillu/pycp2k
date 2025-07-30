from pycp2k.inputsection import InputSection


class _gga_k_lgap5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._mu1 = None
        self._mu2 = None
        self._mu3 = None
        self._name = "GGA_K_LGAP"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_mu1': '_MU1', '_mu2': '_MU2', '_mu3': '_MU3'}
        self._attributes = ['Section_parameters']

