from pycp2k.inputsection import InputSection


class _gga_c_n128(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._css0 = None
        self._css1 = None
        self._css2 = None
        self._css3 = None
        self._css4 = None
        self._cos0 = None
        self._cos1 = None
        self._cos2 = None
        self._cos3 = None
        self._cos4 = None
        self._name = "GGA_C_N12"
        self._keywords = {'Scale': 'SCALE', '_css0': '_CSS0', '_css1': '_CSS1', '_css2': '_CSS2', '_css3': '_CSS3', '_css4': '_CSS4', '_cos0': '_COS0', '_cos1': '_COS1', '_cos2': '_COS2', '_cos3': '_COS3', '_cos4': '_COS4'}
        self._attributes = ['Section_parameters']

