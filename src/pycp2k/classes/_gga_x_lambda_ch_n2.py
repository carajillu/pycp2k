from pycp2k.inputsection import InputSection


class _gga_x_lambda_ch_n2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._n = None
        self._kappa = None
        self._mu = None
        self._name = "GGA_X_LAMBDA_CH_N"
        self._keywords = {'Scale': 'SCALE', '_n': '_N', '_kappa': '_KAPPA', '_mu': '_MU'}
        self._attributes = ['Section_parameters']

