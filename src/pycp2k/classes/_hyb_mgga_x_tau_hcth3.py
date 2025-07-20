from pycp2k.inputsection import InputSection


class _hyb_mgga_x_tau_hcth3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cxl0 = None
        self._cxl1 = None
        self._cxl2 = None
        self._cxl3 = None
        self._cxnl0 = None
        self._cxnl1 = None
        self._cxnl2 = None
        self._cxnl3 = None
        self._ax = None
        self._name = "HYB_MGGA_X_TAU_HCTH"
        self._keywords = {'Scale': 'SCALE', '_cxl0': '_CXL0', '_cxl1': '_CXL1', '_cxl2': '_CXL2', '_cxl3': '_CXL3', '_cxnl0': '_CXNL0', '_cxnl1': '_CXNL1', '_cxnl2': '_CXNL2', '_cxnl3': '_CXNL3', '_ax': '_AX'}
        self._attributes = ['Section_parameters']

