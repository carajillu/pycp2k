from pycp2k.inputsection import InputSection


class _gga_k_vsk5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a0 = None
        self._a1 = None
        self._a2 = None
        self._a3 = None
        self._a4 = None
        self._b0 = None
        self._b1 = None
        self._b2 = None
        self._b3 = None
        self._b4 = None
        self._name = "GGA_K_VSK"
        self._keywords = {'Scale': 'SCALE', '_a0': '_A0', '_a1': '_A1', '_a2': '_A2', '_a3': '_A3', '_a4': '_A4', '_b0': '_B0', '_b1': '_B1', '_b2': '_B2', '_b3': '_B3', '_b4': '_B4'}
        self._attributes = ['Section_parameters']

