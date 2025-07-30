from pycp2k.inputsection import InputSection


class _lda_x_erf7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._omega = None
        self._name = "LDA_X_ERF"
        self._keywords = {'Scale': 'SCALE', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

