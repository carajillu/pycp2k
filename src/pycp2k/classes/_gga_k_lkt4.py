from pycp2k.inputsection import InputSection


class _gga_k_lkt4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._name = "GGA_K_LKT"
        self._keywords = {'Scale': 'SCALE', '_a': '_A'}
        self._attributes = ['Section_parameters']

