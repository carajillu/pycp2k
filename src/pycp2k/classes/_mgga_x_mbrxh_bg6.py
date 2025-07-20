from pycp2k.inputsection import InputSection


class _mgga_x_mbrxh_bg6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_X_MBRXH_BG"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

