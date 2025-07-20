from pycp2k.inputsection import InputSection


class _mgga_k_pgsl0251(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._mu = None
        self._beta = None
        self._name = "MGGA_K_PGSL025"
        self._keywords = {'Scale': 'SCALE', '_mu': '_MU', '_beta': '_BETA'}
        self._attributes = ['Section_parameters']

