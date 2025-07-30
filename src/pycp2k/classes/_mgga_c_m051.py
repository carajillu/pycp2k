from pycp2k.inputsection import InputSection


class _mgga_c_m051(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma_ss = None
        self._gamma_ab = None
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
        self._fermi_d_cnst = None
        self._name = "MGGA_C_M05"
        self._keywords = {'Scale': 'SCALE', '_gamma_ss': '_GAMMA_SS', '_gamma_ab': '_GAMMA_AB', '_css0': '_CSS0', '_css1': '_CSS1', '_css2': '_CSS2', '_css3': '_CSS3', '_css4': '_CSS4', '_cab0': '_CAB0', '_cab1': '_CAB1', '_cab2': '_CAB2', '_cab3': '_CAB3', '_cab4': '_CAB4', '_fermi_d_cnst': '_FERMI_D_CNST'}
        self._attributes = ['Section_parameters']

