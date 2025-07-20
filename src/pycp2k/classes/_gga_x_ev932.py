from pycp2k.inputsection import InputSection


class _gga_x_ev932(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a1 = None
        self._a2 = None
        self._a3 = None
        self._b1 = None
        self._b2 = None
        self._b3 = None
        self._name = "GGA_X_EV93"
        self._keywords = {'Scale': 'SCALE', '_a1': '_A1', '_a2': '_A2', '_a3': '_A3', '_b1': '_B1', '_b2': '_B2', '_b3': '_B3'}
        self._attributes = ['Section_parameters']

