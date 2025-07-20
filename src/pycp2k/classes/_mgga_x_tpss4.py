from pycp2k.inputsection import InputSection


class _mgga_x_tpss4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._b = None
        self._c = None
        self._e = None
        self._kappa = None
        self._mu = None
        self._bloc_a = None
        self._bloc_b = None
        self._name = "MGGA_X_TPSS"
        self._keywords = {'Scale': 'SCALE', '_b': '_B', '_c': '_C', '_e': '_E', '_kappa': '_KAPPA', '_mu': '_MU', '_bloc_a': '_BLOC_A', '_bloc_b': '_BLOC_B'}
        self._attributes = ['Section_parameters']

