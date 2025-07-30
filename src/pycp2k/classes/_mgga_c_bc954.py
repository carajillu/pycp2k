from pycp2k.inputsection import InputSection


class _mgga_c_bc954(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._css = None
        self._copp = None
        self._name = "MGGA_C_BC95"
        self._keywords = {'Scale': 'SCALE', '_css': '_CSS', '_copp': '_COPP'}
        self._attributes = ['Section_parameters']

