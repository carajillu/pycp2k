from pycp2k.inputsection import InputSection


class _lda_x_rae2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.N = None
        self._name = "LDA_X_RAE"
        self._keywords = {'Scale': 'SCALE', 'N': 'N'}
        self._attributes = ['Section_parameters']

