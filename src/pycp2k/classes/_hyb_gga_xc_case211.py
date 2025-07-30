from pycp2k.inputsection import InputSection


class _hyb_gga_xc_case211(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cx0 = None
        self._cx1 = None
        self._cx2 = None
        self._cx3 = None
        self._cx4 = None
        self._cx5 = None
        self._cx6 = None
        self._cx7 = None
        self._cx8 = None
        self._cx9 = None
        self._cc0 = None
        self._cc1 = None
        self._cc2 = None
        self._cc3 = None
        self._cc4 = None
        self._cc5 = None
        self._cc6 = None
        self._cc7 = None
        self._cc8 = None
        self._cc9 = None
        self._gammax = None
        self._gammac = None
        self._ax = None
        self._name = "HYB_GGA_XC_CASE21"
        self._keywords = {'Scale': 'SCALE', '_cx0': '_CX0', '_cx1': '_CX1', '_cx2': '_CX2', '_cx3': '_CX3', '_cx4': '_CX4', '_cx5': '_CX5', '_cx6': '_CX6', '_cx7': '_CX7', '_cx8': '_CX8', '_cx9': '_CX9', '_cc0': '_CC0', '_cc1': '_CC1', '_cc2': '_CC2', '_cc3': '_CC3', '_cc4': '_CC4', '_cc5': '_CC5', '_cc6': '_CC6', '_cc7': '_CC7', '_cc8': '_CC8', '_cc9': '_CC9', '_gammax': '_GAMMAX', '_gammac': '_GAMMAC', '_ax': '_AX'}
        self._attributes = ['Section_parameters']

