from pycp2k.inputsection import InputSection


class _mgga_k_csk44(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._name = "MGGA_K_CSK4"
        self._keywords = {'Scale': 'SCALE', '_a': '_A'}
        self._attributes = ['Section_parameters']

