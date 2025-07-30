from pycp2k.inputsection import InputSection


class _mgga_x_rtpss3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._b = None
        self._c = None
        self._e = None
        self._kappa = None
        self._mu = None
        self._name = "MGGA_X_RTPSS"
        self._keywords = {'Scale': 'SCALE', '_b': '_B', '_c': '_C', '_e': '_E', '_kappa': '_KAPPA', '_mu': '_MU'}
        self._attributes = ['Section_parameters']

