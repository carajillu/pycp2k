from pycp2k.inputsection import InputSection


class _hyb_mgga_x_pjs188(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._omega = None
        self._name = "HYB_MGGA_X_PJS18"
        self._keywords = {'Scale': 'SCALE', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

