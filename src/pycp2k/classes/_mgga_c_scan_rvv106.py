from pycp2k.inputsection import InputSection


class _mgga_c_scan_rvv106(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_C_SCAN_RVV10"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

