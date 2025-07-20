from pycp2k.inputsection import InputSection


class _mgga_x_br89_explicit_13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._name = "MGGA_X_BR89_EXPLICIT_1"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA'}
        self._attributes = ['Section_parameters']

