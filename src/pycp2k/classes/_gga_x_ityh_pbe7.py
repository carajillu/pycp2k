from pycp2k.inputsection import InputSection


class _gga_x_ityh_pbe7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._mu = None
        self._omega = None
        self._name = "GGA_X_ITYH_PBE"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_mu': '_MU', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

