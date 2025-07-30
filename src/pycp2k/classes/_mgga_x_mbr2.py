from pycp2k.inputsection import InputSection


class _mgga_x_mbr2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._beta = None
        self._lambda = None
        self._name = "MGGA_X_MBR"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA', '_beta': '_BETA', '_lambda': '_LAMBDA'}
        self._attributes = ['Section_parameters']

