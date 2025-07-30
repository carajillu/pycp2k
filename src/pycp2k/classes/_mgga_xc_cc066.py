from pycp2k.inputsection import InputSection


class _mgga_xc_cc066(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_XC_CC06"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

