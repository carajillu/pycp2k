from pycp2k.inputsection import InputSection


class _hyb_gga_x_cam_s12g7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._c = None
        self._d = None
        self._e = None
        self._alpha = None
        self._beta = None
        self._omega = None
        self._name = "HYB_GGA_X_CAM_S12G"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B', '_c': '_C', '_d': '_D', '_e': '_E', '_alpha': '_ALPHA', '_beta': '_BETA', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

