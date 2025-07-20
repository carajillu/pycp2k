from pycp2k.inputsection import InputSection
from ._dipole_moments1 import _dipole_moments1
from ._xc6 import _xc6
from ._mgrid2 import _mgrid2
from ._stda1 import _stda1
from ._lrigpw3 import _lrigpw3
from ._print99 import _print99


class _tddfpt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nstates = None
        self.Max_iter = None
        self.Max_kv = None
        self.Nlumo = None
        self.Nproc_state = None
        self.Kernel = None
        self.Oe_corr = None
        self.Ev_shift = None
        self.Eos_shift = None
        self.Convergence = None
        self.Min_amplitude = None
        self.Orthogonal_eps = None
        self.Restart = None
        self.Rks_triplets = None
        self.Admm_kernel_correction_symmetric = None
        self.Do_lrigpw = None
        self.Auto_basis = []
        self.Wfn_restart_file_name = None
        self.DIPOLE_MOMENTS = _dipole_moments1()
        self.XC = _xc6()
        self.MGRID = _mgrid2()
        self.STDA = _stda1()
        self.LRIGPW = _lrigpw3()
        self.PRINT = _print99()
        self._name = "TDDFPT"
        self._keywords = {'Nstates': 'NSTATES', 'Max_iter': 'MAX_ITER', 'Max_kv': 'MAX_KV', 'Nlumo': 'NLUMO', 'Nproc_state': 'NPROC_STATE', 'Kernel': 'KERNEL', 'Oe_corr': 'OE_CORR', 'Ev_shift': 'EV_SHIFT', 'Eos_shift': 'EOS_SHIFT', 'Convergence': 'CONVERGENCE', 'Min_amplitude': 'MIN_AMPLITUDE', 'Orthogonal_eps': 'ORTHOGONAL_EPS', 'Restart': 'RESTART', 'Rks_triplets': 'RKS_TRIPLETS', 'Admm_kernel_correction_symmetric': 'ADMM_KERNEL_CORRECTION_SYMMETRIC', 'Do_lrigpw': 'DO_LRIGPW', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME'}
        self._repeated_keywords = {'Auto_basis': 'AUTO_BASIS'}
        self._subsections = {'DIPOLE_MOMENTS': 'DIPOLE_MOMENTS', 'XC': 'XC', 'MGRID': 'MGRID', 'STDA': 'STDA', 'LRIGPW': 'LRIGPW', 'PRINT': 'PRINT'}
        self._aliases = {'Virtual_shift': 'Ev_shift', 'Open_shell_shift': 'Eos_shift', 'Restart_file_name': 'Wfn_restart_file_name'}
        self._attributes = ['Section_parameters']


    @property
    def Virtual_shift(self):
        """
        See documentation for Ev_shift
        """
        return self.Ev_shift

    @property
    def Open_shell_shift(self):
        """
        See documentation for Eos_shift
        """
        return self.Eos_shift

    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Virtual_shift.setter
    def Virtual_shift(self, value):
        self.Ev_shift = value

    @Open_shell_shift.setter
    def Open_shell_shift(self, value):
        self.Eos_shift = value

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
