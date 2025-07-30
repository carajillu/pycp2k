from pycp2k.inputsection import InputSection


class _gga_xc_pbe1w3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_XC_PBE1W"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

