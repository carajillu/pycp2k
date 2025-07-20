from pycp2k.inputsection import InputSection


class _mgga_x_mk00b5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_X_MK00B"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

