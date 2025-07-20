from pycp2k.inputsection import InputSection


class _lda_c_1d_csc7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.Interaction = None
        self.Beta = None
        self._name = "LDA_C_1D_CSC"
        self._keywords = {'Scale': 'SCALE', 'Interaction': 'INTERACTION', 'Beta': 'BETA'}
        self._attributes = ['Section_parameters']

