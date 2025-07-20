from pycp2k.inputsection import InputSection


class _lda_xc_lp_b8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._name = "LDA_XC_LP_B"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B'}
        self._attributes = ['Section_parameters']

