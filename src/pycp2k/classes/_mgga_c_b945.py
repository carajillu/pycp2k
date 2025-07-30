from pycp2k.inputsection import InputSection


class _mgga_c_b945(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._css = None
        self._cab = None
        self._name = "MGGA_C_B94"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA', '_css': '_CSS', '_cab': '_CAB'}
        self._attributes = ['Section_parameters']

