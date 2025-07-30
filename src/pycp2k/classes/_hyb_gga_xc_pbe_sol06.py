from pycp2k.inputsection import InputSection


class _hyb_gga_xc_pbe_sol06(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._name = "HYB_GGA_XC_PBE_SOL0"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA'}
        self._attributes = ['Section_parameters']

