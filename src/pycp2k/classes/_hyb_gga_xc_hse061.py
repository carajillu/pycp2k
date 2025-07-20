from pycp2k.inputsection import InputSection


class _hyb_gga_xc_hse061(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._omega_hf = None
        self._omega_pbe = None
        self._name = "HYB_GGA_XC_HSE06"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA', '_omega_hf': '_OMEGA_HF', '_omega_pbe': '_OMEGA_PBE'}
        self._attributes = ['Section_parameters']

