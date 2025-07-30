from pycp2k.inputsection import InputSection


class _gga_x_cap6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._alphaoax = None
        self._c = None
        self._name = "GGA_X_CAP"
        self._keywords = {'Scale': 'SCALE', '_alphaoax': '_ALPHAOAX', '_c': '_C'}
        self._attributes = ['Section_parameters']

