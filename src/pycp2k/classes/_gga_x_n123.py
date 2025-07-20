from pycp2k.inputsection import InputSection


class _gga_x_n123(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cc00 = None
        self._cc01 = None
        self._cc02 = None
        self._cc03 = None
        self._cc10 = None
        self._cc11 = None
        self._cc12 = None
        self._cc13 = None
        self._cc20 = None
        self._cc21 = None
        self._cc22 = None
        self._cc23 = None
        self._cc30 = None
        self._cc31 = None
        self._cc32 = None
        self._cc33 = None
        self._name = "GGA_X_N12"
        self._keywords = {'Scale': 'SCALE', '_cc00': '_CC00', '_cc01': '_CC01', '_cc02': '_CC02', '_cc03': '_CC03', '_cc10': '_CC10', '_cc11': '_CC11', '_cc12': '_CC12', '_cc13': '_CC13', '_cc20': '_CC20', '_cc21': '_CC21', '_cc22': '_CC22', '_cc23': '_CC23', '_cc30': '_CC30', '_cc31': '_CC31', '_cc32': '_CC32', '_cc33': '_CC33'}
        self._attributes = ['Section_parameters']

