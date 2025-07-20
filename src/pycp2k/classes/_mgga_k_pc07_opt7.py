from pycp2k.inputsection import InputSection


class _mgga_k_pc07_opt7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._name = "MGGA_K_PC07_OPT"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B'}
        self._attributes = ['Section_parameters']

