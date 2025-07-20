from pycp2k.inputsection import InputSection


class _mgga_xc_lp906(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_XC_LP90"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

