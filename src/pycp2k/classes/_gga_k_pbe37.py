from pycp2k.inputsection import InputSection


class _gga_k_pbe37(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._c1 = None
        self._c2 = None
        self._c3 = None
        self._name = "GGA_K_PBE3"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_c1': '_C1', '_c2': '_C2', '_c3': '_C3'}
        self._attributes = ['Section_parameters']

