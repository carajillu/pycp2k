from pycp2k.inputsection import InputSection


class _mgga_c_m06_sx5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma_ss = None
        self._gamma_ab = None
        self._alpha_ss = None
        self._alpha_ab = None
        self._css0 = None
        self._css1 = None
        self._css2 = None
        self._css3 = None
        self._css4 = None
        self._cab0 = None
        self._cab1 = None
        self._cab2 = None
        self._cab3 = None
        self._cab4 = None
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
        self._fermi_d_cnst = None
        self._name = "MGGA_C_M06_SX"
        self._keywords = {'Scale': 'SCALE', '_gamma_ss': '_GAMMA_SS', '_gamma_ab': '_GAMMA_AB', '_alpha_ss': '_ALPHA_SS', '_alpha_ab': '_ALPHA_AB', '_css0': '_CSS0', '_css1': '_CSS1', '_css2': '_CSS2', '_css3': '_CSS3', '_css4': '_CSS4', '_cab0': '_CAB0', '_cab1': '_CAB1', '_cab2': '_CAB2', '_cab3': '_CAB3', '_cab4': '_CAB4', '_dss0': '_DSS0', '_dss1': '_DSS1', '_dss2': '_DSS2', '_dss3': '_DSS3', '_dss4': '_DSS4', '_dss5': '_DSS5', '_dab0': '_DAB0', '_dab1': '_DAB1', '_dab2': '_DAB2', '_dab3': '_DAB3', '_dab4': '_DAB4', '_dab5': '_DAB5', '_fermi_d_cnst': '_FERMI_D_CNST'}
        self._attributes = ['Section_parameters']

