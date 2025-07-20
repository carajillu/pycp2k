from pycp2k.inputsection import InputSection


class _mgga_c_vsxc7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._alpha_ss = None
        self._alpha_os = None
        self._dss0 = None
        self._dss1 = None
        self._dss2 = None
        self._dss3 = None
        self._dss4 = None
        self._dss5 = None
        self._dab0 = None
        self._dab1 = None
        self._dab2 = None
        self._dab3 = None
        self._dab4 = None
        self._dab5 = None
        self._name = "MGGA_C_VSXC"
        self._keywords = {'Scale': 'SCALE', '_alpha_ss': '_ALPHA_SS', '_alpha_os': '_ALPHA_OS', '_dss0': '_DSS0', '_dss1': '_DSS1', '_dss2': '_DSS2', '_dss3': '_DSS3', '_dss4': '_DSS4', '_dss5': '_DSS5', '_dab0': '_DAB0', '_dab1': '_DAB1', '_dab2': '_DAB2', '_dab3': '_DAB3', '_dab4': '_DAB4', '_dab5': '_DAB5'}
        self._attributes = ['Section_parameters']

