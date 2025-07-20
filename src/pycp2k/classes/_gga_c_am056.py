from pycp2k.inputsection import InputSection


class _gga_c_am056(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._alpha = None
        self._gamma = None
        self._name = "GGA_C_AM05"
        self._keywords = {'Scale': 'SCALE', '_alpha': '_ALPHA', '_gamma': '_GAMMA'}
        self._attributes = ['Section_parameters']

