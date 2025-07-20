from pycp2k.inputsection import InputSection


class _hyb_gga_xc_apbe02(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_GGA_XC_APBE0"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

