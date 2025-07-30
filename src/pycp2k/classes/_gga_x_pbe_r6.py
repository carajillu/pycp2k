from pycp2k.inputsection import InputSection


class _gga_x_pbe_r6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._mu = None
        self._name = "GGA_X_PBE_R"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_mu': '_MU'}
        self._attributes = ['Section_parameters']

