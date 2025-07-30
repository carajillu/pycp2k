from pycp2k.inputsection import InputSection
from ._program_run_info33 import _program_run_info33
from ._restart11 import _restart11
from ._restart_history4 import _restart_history4
from ._current2 import _current2


class _print58(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info33()
        self.RESTART = _restart11()
        self.RESTART_HISTORY = _restart_history4()
        self.CURRENT = _current2()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'CURRENT': 'CURRENT'}

