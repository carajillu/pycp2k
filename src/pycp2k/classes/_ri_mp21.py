from pycp2k.inputsection import InputSection
from ._cphf1 import _cphf1


class _ri_mp21(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Block_size = None
        self.Eps_canonical = None
        self.Free_hfx_buffer = None
        self.Use_old_gradient_code = None
        self.CPHF = _cphf1()
        self._name = "RI_MP2"
        self._keywords = {'Block_size': 'BLOCK_SIZE', 'Eps_canonical': 'EPS_CANONICAL', 'Free_hfx_buffer': 'FREE_HFX_BUFFER', 'Use_old_gradient_code': 'USE_OLD_GRADIENT_CODE'}
        self._subsections = {'CPHF': 'CPHF'}
        self._aliases = {'Message_size': 'Block_size'}
        self._attributes = ['Section_parameters']


    @property
    def Message_size(self):
        """
        See documentation for Block_size
        """
        return self.Block_size

    @Message_size.setter
    def Message_size(self, value):
        self.Block_size = value
