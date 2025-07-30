from pycp2k.inputsection import InputSection


class _lda_x_1d_soft2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.Beta = None
        self._name = "LDA_X_1D_SOFT"
        self._keywords = {'Scale': 'SCALE', 'Beta': 'BETA'}
        self._attributes = ['Section_parameters']

