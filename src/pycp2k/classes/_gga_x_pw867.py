from pycp2k.inputsection import InputSection


class _gga_x_pw867(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._aa = None
        self._bb = None
        self._cc = None
        self._name = "GGA_X_PW86"
        self._keywords = {'Scale': 'SCALE', '_aa': '_AA', '_bb': '_BB', '_cc': '_CC'}
        self._attributes = ['Section_parameters']

