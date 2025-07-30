from pycp2k.inputsection import InputSection
from ._xc2 import _xc2
from ._response_solver1 import _response_solver1
from ._print37 import _print37


class _energy_correction1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Energy_functional = None
        self.Harris_basis = None
        self.Skip_ec = None
        self.Mao = None
        self.Mao_max_iter = None
        self.Mao_eps_grad = None
        self.Mao_eps1 = None
        self.Mao_iolevel = None
        self.Algorithm = None
        self.Factorization = None
        self.Eps_default = None
        self.Eps_filter = None
        self.Eps_lanczos = None
        self.Max_iter_lanczos = None
        self.Mu = None
        self.Fixed_mu = None
        self.S_preconditioner = None
        self.S_sqrt_method = None
        self.S_sqrt_order = None
        self.Sign_method = None
        self.Sign_order = None
        self.Dynamic_threshold = None
        self.Non_monotonic = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.S_inversion = None
        self.Report_all_sparsities = None
        self.Check_s_inv = None
        self.Ot_initial_guess = None
        self.XC = _xc2()
        self.RESPONSE_SOLVER = _response_solver1()
        self.PRINT = _print37()
        self._name = "ENERGY_CORRECTION"
        self._keywords = {'Energy_functional': 'ENERGY_FUNCTIONAL', 'Harris_basis': 'HARRIS_BASIS', 'Skip_ec': 'SKIP_EC', 'Mao': 'MAO', 'Mao_max_iter': 'MAO_MAX_ITER', 'Mao_eps_grad': 'MAO_EPS_GRAD', 'Mao_eps1': 'MAO_EPS1', 'Mao_iolevel': 'MAO_IOLEVEL', 'Algorithm': 'ALGORITHM', 'Factorization': 'FACTORIZATION', 'Eps_default': 'EPS_DEFAULT', 'Eps_filter': 'EPS_FILTER', 'Eps_lanczos': 'EPS_LANCZOS', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Mu': 'MU', 'Fixed_mu': 'FIXED_MU', 'S_preconditioner': 'S_PRECONDITIONER', 'S_sqrt_method': 'S_SQRT_METHOD', 'S_sqrt_order': 'S_SQRT_ORDER', 'Sign_method': 'SIGN_METHOD', 'Sign_order': 'SIGN_ORDER', 'Dynamic_threshold': 'DYNAMIC_THRESHOLD', 'Non_monotonic': 'NON_MONOTONIC', 'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'S_inversion': 'S_INVERSION', 'Report_all_sparsities': 'REPORT_ALL_SPARSITIES', 'Check_s_inv': 'CHECK_S_INV', 'Ot_initial_guess': 'OT_INITIAL_GUESS'}
        self._subsections = {'XC': 'XC', 'RESPONSE_SOLVER': 'RESPONSE_SOLVER', 'PRINT': 'PRINT'}
        self._aliases = {'Sign_sqrt_order': 'S_sqrt_order'}
        self._attributes = ['Section_parameters']


    @property
    def Sign_sqrt_order(self):
        """
        See documentation for S_sqrt_order
        """
        return self.S_sqrt_order

    @Sign_sqrt_order.setter
    def Sign_sqrt_order(self, value):
        self.S_sqrt_order = value
