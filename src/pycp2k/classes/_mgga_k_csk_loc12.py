from pycp2k.inputsection import InputSection


class _mgga_k_csk_loc12(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._cp = None
        self._cq = None
        self._name = "MGGA_K_CSK_LOC1"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_cp': '_CP', '_cq': '_CQ'}
        self._attributes = ['Section_parameters']

