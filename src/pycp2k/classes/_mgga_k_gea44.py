from pycp2k.inputsection import InputSection


class _mgga_k_gea44(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_K_GEA4"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

