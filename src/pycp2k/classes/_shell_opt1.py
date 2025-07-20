from pycp2k.inputsection import InputSection
from ._lbfgs4 import _lbfgs4
from ._cg4 import _cg4
from ._bfgs4 import _bfgs4
from ._print5 import _print5


class _shell_opt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Optimizer = None
        self.Max_iter = None
        self.Max_dr = None
        self.Max_force = None
        self.Rms_dr = None
        self.Rms_force = None
        self.Step_start_val = None
        self.Keep_space_group = None
        self.Eps_symmetry = None
        self.Symm_reduction = None
        self.Symm_exclude_range = []
        self.Spgr_print_atoms = None
        self.LBFGS = _lbfgs4()
        self.CG = _cg4()
        self.BFGS = _bfgs4()
        self.PRINT_list = []
        self._name = "SHELL_OPT"
        self._keywords = {'Optimizer': 'OPTIMIZER', 'Max_iter': 'MAX_ITER', 'Max_dr': 'MAX_DR', 'Max_force': 'MAX_FORCE', 'Rms_dr': 'RMS_DR', 'Rms_force': 'RMS_FORCE', 'Step_start_val': 'STEP_START_VAL', 'Keep_space_group': 'KEEP_SPACE_GROUP', 'Eps_symmetry': 'EPS_SYMMETRY', 'Symm_reduction': 'SYMM_REDUCTION', 'Spgr_print_atoms': 'SPGR_PRINT_ATOMS'}
        self._repeated_keywords = {'Symm_exclude_range': 'SYMM_EXCLUDE_RANGE'}
        self._subsections = {'LBFGS': 'LBFGS', 'CG': 'CG', 'BFGS': 'BFGS'}
        self._repeated_subsections = {'PRINT': '_print5'}
        self._aliases = {'Minimizer': 'Optimizer'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section


    @property
    def Minimizer(self):
        """
        See documentation for Optimizer
        """
        return self.Optimizer

    @Minimizer.setter
    def Minimizer(self, value):
        self.Optimizer = value
