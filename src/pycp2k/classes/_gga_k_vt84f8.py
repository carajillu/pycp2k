from pycp2k.inputsection import InputSection


class _gga_k_vt84f8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._mu = None
        self._alpha = None
        self._name = "GGA_K_VT84F"
        self._keywords = {'Scale': 'SCALE', '_mu': '_MU', '_alpha': '_ALPHA'}
        self._attributes = ['Section_parameters']

