from pycp2k.inputsection import InputSection


class _lda_xc_corrksdt7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.T = None
        self._name = "LDA_XC_CORRKSDT"
        self._keywords = {'Scale': 'SCALE', 'T': 'T'}
        self._attributes = ['Section_parameters']

