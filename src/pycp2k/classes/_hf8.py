from pycp2k.inputsection import InputSection
from ._hf_info8 import _hf_info8
from ._periodic8 import _periodic8
from ._screening9 import _screening9
from ._interaction_potential11 import _interaction_potential11
from ._load_balance8 import _load_balance8
from ._memory9 import _memory9
from ._ri11 import _ri11


class _hf8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info8()
        self.PERIODIC = _periodic8()
        self.SCREENING = _screening9()
        self.INTERACTION_POTENTIAL = _interaction_potential11()
        self.LOAD_BALANCE = _load_balance8()
        self.MEMORY = _memory9()
        self.RI = _ri11()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

