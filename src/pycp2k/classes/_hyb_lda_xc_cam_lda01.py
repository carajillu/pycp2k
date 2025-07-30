from pycp2k.inputsection import InputSection


class _hyb_lda_xc_cam_lda01(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_LDA_XC_CAM_LDA0"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

