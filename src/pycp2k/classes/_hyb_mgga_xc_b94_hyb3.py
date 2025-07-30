from pycp2k.inputsection import InputSection


class _hyb_mgga_xc_b94_hyb3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._gamma = None
        self._css = None
        self._cab = None
        self._cx = None
        self._name = "HYB_MGGA_XC_B94_HYB"
        self._keywords = {'Scale': 'SCALE', '_gamma': '_GAMMA', '_css': '_CSS', '_cab': '_CAB', '_cx': '_CX'}
        self._attributes = ['Section_parameters']

