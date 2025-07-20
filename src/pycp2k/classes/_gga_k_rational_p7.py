from pycp2k.inputsection import InputSection


class _gga_k_rational_p7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c2 = None
        self._p = None
        self._name = "GGA_K_RATIONAL_P"
        self._keywords = {'Scale': 'SCALE', '_c2': '_C2', '_p': '_P'}
        self._attributes = ['Section_parameters']

