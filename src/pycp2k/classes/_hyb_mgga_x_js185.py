from pycp2k.inputsection import InputSection


class _hyb_mgga_x_js185(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._omega = None
        self._name = "HYB_MGGA_X_JS18"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

