from pycp2k.inputsection import InputSection


class _mgga_x_lta4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._ltafrac = None
        self._name = "MGGA_X_LTA"
        self._keywords = {'Scale': 'SCALE', '_ltafrac': '_LTAFRAC'}
        self._attributes = ['Section_parameters']

