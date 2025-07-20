from pycp2k.inputsection import InputSection


class _mgga_x_rppscan8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c2 = None
        self._d = None
        self._k1 = None
        self._eta = None
        self._name = "MGGA_X_RPPSCAN"
        self._keywords = {'Scale': 'SCALE', '_c2': '_C2', '_d': '_D', '_k1': '_K1', '_eta': '_ETA'}
        self._attributes = ['Section_parameters']

