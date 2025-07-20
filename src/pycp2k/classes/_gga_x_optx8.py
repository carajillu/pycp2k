from pycp2k.inputsection import InputSection


class _gga_x_optx8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._gamma = None
        self._name = "GGA_X_OPTX"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_gamma': '_GAMMA'}
        self._attributes = ['Section_parameters']

