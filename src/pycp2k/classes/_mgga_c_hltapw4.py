from pycp2k.inputsection import InputSection


class _mgga_c_hltapw4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._ltafrac = None
        self._name = "MGGA_C_HLTAPW"
        self._keywords = {'Scale': 'SCALE', '_ltafrac': '_LTAFRAC'}
        self._attributes = ['Section_parameters']

