from pycp2k.inputsection import InputSection


class _lda_c_lp968(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c1 = None
        self._c2 = None
        self._c3 = None
        self._name = "LDA_C_LP96"
        self._keywords = {'Scale': 'SCALE', '_c1': '_C1', '_c2': '_C2', '_c3': '_C3'}
        self._attributes = ['Section_parameters']

