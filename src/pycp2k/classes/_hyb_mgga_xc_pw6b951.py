from pycp2k.inputsection import InputSection


class _hyb_mgga_xc_pw6b951(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_MGGA_XC_PW6B95"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

