from pycp2k.inputsection import InputSection


class _hyb_mgga_x_revscan01(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._exx = None
        self._name = "HYB_MGGA_X_REVSCAN0"
        self._keywords = {'Scale': 'SCALE', '_exx': '_EXX'}
        self._attributes = ['Section_parameters']

