from pycp2k.inputsection import InputSection


class _lda_c_vbh3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._r0 = None
        self._r1 = None
        self._c0 = None
        self._c1 = None
        self._name = "LDA_C_VBH"
        self._keywords = {'Scale': 'SCALE', '_r0': '_R0', '_r1': '_R1', '_c0': '_C0', '_c1': '_C1'}
        self._attributes = ['Section_parameters']

