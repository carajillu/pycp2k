from pycp2k.inputsection import InputSection


class _mgga_x_mvsb7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._e1 = None
        self._c1 = None
        self._k0 = None
        self._b = None
        self._name = "MGGA_X_MVSB"
        self._keywords = {'Scale': 'SCALE', '_e1': '_E1', '_c1': '_C1', '_k0': '_K0', '_b': '_B'}
        self._attributes = ['Section_parameters']

