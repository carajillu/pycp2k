from pycp2k.inputsection import InputSection
from ._mp27 import _mp27
from ._ri_mp27 import _ri_mp27
from ._ri_rpa7 import _ri_rpa7
from ._ri_sos_mp27 import _ri_sos_mp27
from ._low_scaling7 import _low_scaling7
from ._ri21 import _ri21
from ._integrals7 import _integrals7
from ._print112 import _print112


class _wf_correlation7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.MP2 = _mp27()
        self.RI_MP2 = _ri_mp27()
        self.RI_RPA = _ri_rpa7()
        self.RI_SOS_MP2 = _ri_sos_mp27()
        self.LOW_SCALING = _low_scaling7()
        self.RI = _ri21()
        self.INTEGRALS = _integrals7()
        self.PRINT = _print112()
        self._name = "WF_CORRELATION"
        self._keywords = {'Memory': 'MEMORY', 'Scale_s': 'SCALE_S', 'Scale_t': 'SCALE_T', 'Group_size': 'GROUP_SIZE'}
        self._subsections = {'MP2': 'MP2', 'RI_MP2': 'RI_MP2', 'RI_RPA': 'RI_RPA', 'RI_SOS_MP2': 'RI_SOS_MP2', 'LOW_SCALING': 'LOW_SCALING', 'RI': 'RI', 'INTEGRALS': 'INTEGRALS', 'PRINT': 'PRINT'}
        self._aliases = {'Number_proc': 'Group_size'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value
