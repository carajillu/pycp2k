from pycp2k.inputsection import InputSection


class _lda_c_pw_rpa1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._pp_0 = None
        self._pp_1 = None
        self._pp_2 = None
        self._a_0 = None
        self._a_1 = None
        self._a_2 = None
        self._alpha1_0 = None
        self._alpha1_1 = None
        self._alpha1_2 = None
        self._beta1_0 = None
        self._beta1_1 = None
        self._beta1_2 = None
        self._beta2_0 = None
        self._beta2_1 = None
        self._beta2_2 = None
        self._beta3_0 = None
        self._beta3_1 = None
        self._beta3_2 = None
        self._beta4_0 = None
        self._beta4_1 = None
        self._beta4_2 = None
        self._fz20 = None
        self._name = "LDA_C_PW_RPA"
        self._keywords = {'Scale': 'SCALE', '_pp_0': '_PP[0]', '_pp_1': '_PP[1]', '_pp_2': '_PP[2]', '_a_0': '_A[0]', '_a_1': '_A[1]', '_a_2': '_A[2]', '_alpha1_0': '_ALPHA1[0]', '_alpha1_1': '_ALPHA1[1]', '_alpha1_2': '_ALPHA1[2]', '_beta1_0': '_BETA1[0]', '_beta1_1': '_BETA1[1]', '_beta1_2': '_BETA1[2]', '_beta2_0': '_BETA2[0]', '_beta2_1': '_BETA2[1]', '_beta2_2': '_BETA2[2]', '_beta3_0': '_BETA3[0]', '_beta3_1': '_BETA3[1]', '_beta3_2': '_BETA3[2]', '_beta4_0': '_BETA4[0]', '_beta4_1': '_BETA4[1]', '_beta4_2': '_BETA4[2]', '_fz20': '_FZ20'}
        self._attributes = ['Section_parameters']

