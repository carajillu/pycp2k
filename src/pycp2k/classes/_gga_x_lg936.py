from pycp2k.inputsection import InputSection


class _gga_x_lg936(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_X_LG93"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

