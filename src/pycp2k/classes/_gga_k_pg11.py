from pycp2k.inputsection import InputSection


class _gga_k_pg11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._mu = None
        self._name = "GGA_K_PG1"
        self._keywords = {'Scale': 'SCALE', '_mu': '_MU'}
        self._attributes = ['Section_parameters']

