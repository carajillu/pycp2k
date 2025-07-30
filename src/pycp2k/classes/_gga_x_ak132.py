from pycp2k.inputsection import InputSection


class _gga_x_ak132(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._b1 = None
        self._b2 = None
        self._name = "GGA_X_AK13"
        self._keywords = {'Scale': 'SCALE', '_b1': '_B1', '_b2': '_B2'}
        self._attributes = ['Section_parameters']

