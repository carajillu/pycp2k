from pycp2k.inputsection import InputSection


class _hyb_gga_xc_edf25(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_GGA_XC_EDF2"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

