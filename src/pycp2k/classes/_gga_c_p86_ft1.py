from pycp2k.inputsection import InputSection


class _gga_c_p86_ft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._malpha = None
        self._mbeta = None
        self._mgamma = None
        self._mdelta = None
        self._aa = None
        self._bb = None
        self._ftilde = None
        self._name = "GGA_C_P86_FT"
        self._keywords = {'Scale': 'SCALE', '_malpha': '_MALPHA', '_mbeta': '_MBETA', '_mgamma': '_MGAMMA', '_mdelta': '_MDELTA', '_aa': '_AA', '_bb': '_BB', '_ftilde': '_FTILDE'}
        self._attributes = ['Section_parameters']

