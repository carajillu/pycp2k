from pycp2k.inputsection import InputSection


class _mgga_c_tm3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._d = None
        self._c0_c0 = None
        self._c0_c1 = None
        self._c0_c2 = None
        self._c0_c3 = None
        self._name = "MGGA_C_TM"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA', '_d': '_D', '_c0_c0': '_C0_C0', '_c0_c1': '_C0_C1', '_c0_c2': '_C0_C2', '_c0_c3': '_C0_C3'}
        self._attributes = ['Section_parameters']

