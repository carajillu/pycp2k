from pycp2k.inputsection import InputSection


class _lda_c_ml16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._fc = None
        self._q = None
        self._name = "LDA_C_ML1"
        self._keywords = {'Scale': 'SCALE', '_fc': '_FC', '_q': '_Q'}
        self._attributes = ['Section_parameters']

