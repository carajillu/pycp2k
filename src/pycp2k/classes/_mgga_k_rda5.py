from pycp2k.inputsection import InputSection


class _mgga_k_rda5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._a1 = None
        self._a2 = None
        self._a3 = None
        self._beta1 = None
        self._beta2 = None
        self._beta3 = None
        self._a = None
        self._b = None
        self._c = None
        self._name = "MGGA_K_RDA"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_a1': '_A1', '_a2': '_A2', '_a3': '_A3', '_beta1': '_BETA1', '_beta2': '_BETA2', '_beta3': '_BETA3', '_a': '_A', '_b': '_B', '_c': '_C'}
        self._attributes = ['Section_parameters']

