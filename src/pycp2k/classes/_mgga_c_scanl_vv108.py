from pycp2k.inputsection import InputSection


class _mgga_c_scanl_vv108(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_C_SCANL_VV10"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

