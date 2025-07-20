from pycp2k.inputsection import InputSection


class _hyb_mgga_x_mvsh7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_MGGA_X_MVSH"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

