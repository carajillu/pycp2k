from pycp2k.inputsection import InputSection


class _gga_x_b88m1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._gamma = None
        self._name = "GGA_X_B88M"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA', '_gamma': '_GAMMA'}
        self._attributes = ['Section_parameters']

