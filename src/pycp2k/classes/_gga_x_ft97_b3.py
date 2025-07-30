from pycp2k.inputsection import InputSection


class _gga_x_ft97_b3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta0 = None
        self._beta1 = None
        self._beta2 = None
        self._name = "GGA_X_FT97_B"
        self._keywords = {'Scale': 'SCALE', '_beta0': '_BETA0', '_beta1': '_BETA1', '_beta2': '_BETA2'}
        self._attributes = ['Section_parameters']

