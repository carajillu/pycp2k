from pycp2k.inputsection import InputSection
from ._hf_info14 import _hf_info14
from ._periodic15 import _periodic15
from ._screening15 import _screening15
from ._interaction_potential20 import _interaction_potential20
from ._load_balance14 import _load_balance14
from ._memory15 import _memory15
from ._ri20 import _ri20


class _hf14(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info14()
        self.PERIODIC = _periodic15()
        self.SCREENING = _screening15()
        self.INTERACTION_POTENTIAL = _interaction_potential20()
        self.LOAD_BALANCE = _load_balance14()
        self.MEMORY = _memory15()
        self.RI = _ri20()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

