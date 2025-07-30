from pycp2k.inputsection import InputSection


class _gga_k_ludena6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.N = None
        self._name = "GGA_K_LUDENA"
        self._keywords = {'Scale': 'SCALE', 'N': 'N'}
        self._attributes = ['Section_parameters']

