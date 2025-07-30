from pycp2k.inputsection import InputSection


class _response_solver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps = None
        self.Eps_filter = None
        self.Eps_lanczos = None
        self.Max_iter = None
        self.Max_iter_lanczos = None
        self.Method = None
        self.Preconditioner = None
        self.S_preconditioner = None
        self.S_sqrt_method = None
        self.S_sqrt_order = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.S_inversion = None
        self.Restart = None
        self.Restart_every = None
        self._name = "RESPONSE_SOLVER"
        self._keywords = {'Eps': 'EPS', 'Eps_filter': 'EPS_FILTER', 'Eps_lanczos': 'EPS_LANCZOS', 'Max_iter': 'MAX_ITER', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Method': 'METHOD', 'Preconditioner': 'PRECONDITIONER', 'S_preconditioner': 'S_PRECONDITIONER', 'S_sqrt_method': 'S_SQRT_METHOD', 'S_sqrt_order': 'S_SQRT_ORDER', 'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'S_inversion': 'S_INVERSION', 'Restart': 'RESTART', 'Restart_every': 'RESTART_EVERY'}
        self._aliases = {'Sign_sqrt_order': 'S_sqrt_order'}


    @property
    def Sign_sqrt_order(self):
        """
        See documentation for S_sqrt_order
        """
        return self.S_sqrt_order

    @Sign_sqrt_order.setter
    def Sign_sqrt_order(self, value):
        self.S_sqrt_order = value
