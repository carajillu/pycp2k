from pycp2k.inputsection import InputSection


class _gga_x_optb86b_vdw5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._gamma = None
        self._omega = None
        self._name = "GGA_X_OPTB86B_VDW"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA', '_gamma': '_GAMMA', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

