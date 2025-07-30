from pycp2k.inputsection import InputSection


class _lda_c_xalpha8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.Alpha = None
        self._name = "LDA_C_XALPHA"
        self._keywords = {'Scale': 'SCALE', 'Alpha': 'ALPHA'}
        self._attributes = ['Section_parameters']

