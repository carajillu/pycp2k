from pycp2k.inputsection import InputSection


class _gga_xc_th_fc4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._w_0 = None
        self._w_1 = None
        self._w_2 = None
        self._w_3 = None
        self._w_4 = None
        self._w_5 = None
        self._w_6 = None
        self._w_7 = None
        self._w_8 = None
        self._w_9 = None
        self._w_10 = None
        self._w_11 = None
        self._w_12 = None
        self._w_13 = None
        self._w_14 = None
        self._w_15 = None
        self._w_16 = None
        self._w_17 = None
        self._w_18 = None
        self._w_19 = None
        self._w_20 = None
        self._name = "GGA_XC_TH_FC"
        self._keywords = {'Scale': 'SCALE', '_w_0': '_W[0]', '_w_1': '_W[1]', '_w_2': '_W[2]', '_w_3': '_W[3]', '_w_4': '_W[4]', '_w_5': '_W[5]', '_w_6': '_W[6]', '_w_7': '_W[7]', '_w_8': '_W[8]', '_w_9': '_W[9]', '_w_10': '_W[10]', '_w_11': '_W[11]', '_w_12': '_W[12]', '_w_13': '_W[13]', '_w_14': '_W[14]', '_w_15': '_W[15]', '_w_16': '_W[16]', '_w_17': '_W[17]', '_w_18': '_W[18]', '_w_19': '_W[19]', '_w_20': '_W[20]'}
        self._attributes = ['Section_parameters']

