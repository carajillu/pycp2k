from pycp2k.inputsection import InputSection


class _lda_c_1d_loos1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "LDA_C_1D_LOOS"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

