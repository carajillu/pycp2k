from pycp2k.inputsection import InputSection


class _gga_k_tfvw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._lambda = None
        self._gamma = None
        self._name = "GGA_K_TFVW"
        self._keywords = {'Scale': 'SCALE', '_lambda': '_LAMBDA', '_gamma': '_GAMMA'}
        self._attributes = ['Section_parameters']

