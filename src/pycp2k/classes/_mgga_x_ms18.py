from pycp2k.inputsection import InputSection


class _mgga_x_ms18(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._c = None
        self._b = None
        self._name = "MGGA_X_MS1"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_c': '_C', '_b': '_B'}
        self._attributes = ['Section_parameters']

