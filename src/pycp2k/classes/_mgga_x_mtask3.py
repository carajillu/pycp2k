from pycp2k.inputsection import InputSection


class _mgga_x_mtask3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c = None
        self._d = None
        self._h0x = None
        self._anu0 = None
        self._anu1 = None
        self._anu2 = None
        self._bnu0 = None
        self._bnu1 = None
        self._bnu2 = None
        self._bnu3 = None
        self._bnu4 = None
        self._name = "MGGA_X_MTASK"
        self._keywords = {'Scale': 'SCALE', '_c': '_C', '_d': '_D', '_h0x': '_H0X', '_anu0': '_ANU0', '_anu1': '_ANU1', '_anu2': '_ANU2', '_bnu0': '_BNU0', '_bnu1': '_BNU1', '_bnu2': '_BNU2', '_bnu3': '_BNU3', '_bnu4': '_BNU4'}
        self._attributes = ['Section_parameters']

