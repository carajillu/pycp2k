from pycp2k.inputsection import InputSection


class _mgga_x_gx1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c0 = None
        self._c1 = None
        self._alphainf = None
        self._name = "MGGA_X_GX"
        self._keywords = {'Scale': 'SCALE', '_c0': '_C0', '_c1': '_C1', '_alphainf': '_ALPHAINF'}
        self._attributes = ['Section_parameters']

