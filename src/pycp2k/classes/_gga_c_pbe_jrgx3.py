from pycp2k.inputsection import InputSection


class _gga_c_pbe_jrgx3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._gamma = None
        self._b = None
        self._name = "GGA_C_PBE_JRGX"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA', '_gamma': '_GAMMA', '_b': '_B'}
        self._attributes = ['Section_parameters']

