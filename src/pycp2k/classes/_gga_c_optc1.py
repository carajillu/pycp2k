from pycp2k.inputsection import InputSection


class _gga_c_optc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c1 = None
        self._c2 = None
        self._name = "GGA_C_OPTC"
        self._keywords = {'Scale': 'SCALE', '_c1': '_C1', '_c2': '_C2'}
        self._attributes = ['Section_parameters']

