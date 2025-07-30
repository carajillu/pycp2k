from pycp2k.inputsection import InputSection


class _lda_x_sloc3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._a = None
        self._b = None
        self._name = "LDA_X_SLOC"
        self._keywords = {'Scale': 'SCALE', '_a': '_A', '_b': '_B'}
        self._attributes = ['Section_parameters']

