from pycp2k.inputsection import InputSection


class _mgga_xc_b97m_v7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_XC_B97M_V"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

