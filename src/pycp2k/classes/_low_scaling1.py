from pycp2k.inputsection import InputSection


class _low_scaling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Memory_cut = None
        self.Memory_info = None
        self.Eps_filter = None
        self.Eps_filter_factor = None
        self.Eps_storage_scaling = None
        self.Do_kpoints = None
        self.Kpoints = None
        self.Kpoint_weights_w = None
        self.Exponent_tailored_weights = None
        self.Rel_cutoffs_chi_w = None
        self.Regularization_ri = None
        self.Make_chi_pos_definite = None
        self.K_mesh_g_factor = None
        self.Min_block_size = None
        self.Min_block_size_mo = None
        self._name = "LOW_SCALING"
        self._keywords = {'Memory_cut': 'MEMORY_CUT', 'Memory_info': 'MEMORY_INFO', 'Eps_filter': 'EPS_FILTER', 'Eps_filter_factor': 'EPS_FILTER_FACTOR', 'Eps_storage_scaling': 'EPS_STORAGE_SCALING', 'Do_kpoints': 'DO_KPOINTS', 'Kpoints': 'KPOINTS', 'Kpoint_weights_w': 'KPOINT_WEIGHTS_W', 'Exponent_tailored_weights': 'EXPONENT_TAILORED_WEIGHTS', 'Rel_cutoffs_chi_w': 'REL_CUTOFFS_CHI_W', 'Regularization_ri': 'REGULARIZATION_RI', 'Make_chi_pos_definite': 'MAKE_CHI_POS_DEFINITE', 'K_mesh_g_factor': 'K_MESH_G_FACTOR', 'Min_block_size': 'MIN_BLOCK_SIZE', 'Min_block_size_mo': 'MIN_BLOCK_SIZE_MO'}
        self._aliases = {'Eps_storage': 'Eps_storage_scaling'}
        self._attributes = ['Section_parameters']


    @property
    def Eps_storage(self):
        """
        See documentation for Eps_storage_scaling
        """
        return self.Eps_storage_scaling

    @Eps_storage.setter
    def Eps_storage(self, value):
        self.Eps_storage_scaling = value
