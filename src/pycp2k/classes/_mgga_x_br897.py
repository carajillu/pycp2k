from pycp2k.inputsection import InputSection


class _mgga_x_br897(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._at = None
        self._name = "MGGA_X_BR89"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA', '_at': '_AT'}
        self._attributes = ['Section_parameters']

