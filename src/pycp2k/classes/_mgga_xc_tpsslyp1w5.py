from pycp2k.inputsection import InputSection


class _mgga_xc_tpsslyp1w5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_XC_TPSSLYP1W"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

