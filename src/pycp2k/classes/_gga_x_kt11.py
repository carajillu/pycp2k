from pycp2k.inputsection import InputSection


class _gga_x_kt11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._delta = None
        self._name = "GGA_X_KT1"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA', '_delta': '_DELTA'}
        self._attributes = ['Section_parameters']

