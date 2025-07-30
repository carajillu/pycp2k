from pycp2k.inputsection import InputSection


class _gga_c_lm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._f = None
        self._name = "GGA_C_LM"
        self._keywords = {'Scale': 'SCALE', '_f': '_F'}
        self._attributes = ['Section_parameters']

