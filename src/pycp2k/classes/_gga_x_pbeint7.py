from pycp2k.inputsection import InputSection


class _gga_x_pbeint7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._alpha = None
        self._mupbe = None
        self._muge = None
        self._name = "GGA_X_PBEINT"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA', '_alpha': '_ALPHA', '_mupbe': '_MUPBE', '_muge': '_MUGE'}
        self._attributes = ['Section_parameters']

