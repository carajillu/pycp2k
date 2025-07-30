from pycp2k.inputsection import InputSection


class _lda_c_pz6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma0 = None
        self._gamma1 = None
        self._beta10 = None
        self._beta11 = None
        self._beta20 = None
        self._beta21 = None
        self._a0 = None
        self._a1 = None
        self._b0 = None
        self._b1 = None
        self._c0 = None
        self._c1 = None
        self._d0 = None
        self._d1 = None
        self._name = "LDA_C_PZ"
        self._keywords = {'Scale': 'SCALE', '_gamma0': '_GAMMA0', '_gamma1': '_GAMMA1', '_beta10': '_BETA10', '_beta11': '_BETA11', '_beta20': '_BETA20', '_beta21': '_BETA21', '_a0': '_A0', '_a1': '_A1', '_b0': '_B0', '_b1': '_B1', '_c0': '_C0', '_c1': '_C1', '_d0': '_D0', '_d1': '_D1'}
        self._attributes = ['Section_parameters']

