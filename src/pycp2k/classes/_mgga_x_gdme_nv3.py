from pycp2k.inputsection import InputSection


class _mgga_x_gdme_nv3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._aa = None
        self._bb = None
        self._name = "MGGA_X_GDME_NV"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_aa': '_AA', '_bb': '_BB'}
        self._attributes = ['Section_parameters']

