from pycp2k.inputsection import InputSection


class _lda_c_2d_amgb3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "LDA_C_2D_AMGB"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

