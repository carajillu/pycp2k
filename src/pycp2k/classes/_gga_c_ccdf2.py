from pycp2k.inputsection import InputSection


class _gga_c_ccdf2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c1 = None
        self._c2 = None
        self._c3 = None
        self._c4 = None
        self._c5 = None
        self._name = "GGA_C_CCDF"
        self._keywords = {'Scale': 'SCALE', '_c1': '_C1', '_c2': '_C2', '_c3': '_C3', '_c4': '_C4', '_c5': '_C5'}
        self._attributes = ['Section_parameters']

