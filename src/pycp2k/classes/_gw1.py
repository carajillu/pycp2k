from pycp2k.inputsection import InputSection
from ._periodic_correction1 import _periodic_correction1
from ._bse1 import _bse1
from ._ic1 import _ic1
from ._print28 import _print28
from ._kpoint_set1 import _kpoint_set1


class _gw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Corr_mos_occ = None
        self.Corr_mos_virt = None
        self.Numb_poles = None
        self.Omega_max_fit = None
        self.Crossing_search = None
        self.Fermi_level_offset = None
        self.Ev_gw_iter = None
        self.Sc_gw0_iter = None
        self.Eps_iter = None
        self.Print_exx = None
        self.Ri_sigma_x = None
        self.Ic_corr_list = None
        self.Ic_corr_list_beta = None
        self.Periodic_correction = None
        self.Bse = None
        self.Image_charge_model = None
        self.Analytic_continuation = None
        self.Nparam_pade = None
        self.Gamma_only_sigma = None
        self.Update_xc_energy = None
        self.PERIODIC_CORRECTION = _periodic_correction1()
        self.BSE = _bse1()
        self.IC = _ic1()
        self.PRINT = _print28()
        self.KPOINT_SET_list = []
        self._name = "GW"
        self._keywords = {'Corr_mos_occ': 'CORR_MOS_OCC', 'Corr_mos_virt': 'CORR_MOS_VIRT', 'Numb_poles': 'NUMB_POLES', 'Omega_max_fit': 'OMEGA_MAX_FIT', 'Crossing_search': 'CROSSING_SEARCH', 'Fermi_level_offset': 'FERMI_LEVEL_OFFSET', 'Ev_gw_iter': 'EV_GW_ITER', 'Sc_gw0_iter': 'SC_GW0_ITER', 'Eps_iter': 'EPS_ITER', 'Print_exx': 'PRINT_EXX', 'Ri_sigma_x': 'RI_SIGMA_X', 'Ic_corr_list': 'IC_CORR_LIST', 'Ic_corr_list_beta': 'IC_CORR_LIST_BETA', 'Periodic_correction': 'PERIODIC_CORRECTION', 'Bse': 'BSE', 'Image_charge_model': 'IMAGE_CHARGE_MODEL', 'Analytic_continuation': 'ANALYTIC_CONTINUATION', 'Nparam_pade': 'NPARAM_PADE', 'Gamma_only_sigma': 'GAMMA_ONLY_SIGMA', 'Update_xc_energy': 'UPDATE_XC_ENERGY'}
        self._subsections = {'PERIODIC_CORRECTION': 'PERIODIC_CORRECTION', 'BSE': 'BSE', 'IC': 'IC', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'KPOINT_SET': '_kpoint_set1'}
        self._aliases = {'Corr_occ': 'Corr_mos_occ', 'Corr_virt': 'Corr_mos_virt', 'Ic': 'Image_charge_model', 'Gamma': 'Gamma_only_sigma'}
        self._attributes = ['Section_parameters', 'KPOINT_SET_list']

    def KPOINT_SET_add(self, section_parameters=None):
        new_section = _kpoint_set1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KPOINT_SET_list.append(new_section)
        return new_section


    @property
    def Corr_occ(self):
        """
        See documentation for Corr_mos_occ
        """
        return self.Corr_mos_occ

    @property
    def Corr_virt(self):
        """
        See documentation for Corr_mos_virt
        """
        return self.Corr_mos_virt

    @property
    def Ic(self):
        """
        See documentation for Image_charge_model
        """
        return self.Image_charge_model

    @property
    def Gamma(self):
        """
        See documentation for Gamma_only_sigma
        """
        return self.Gamma_only_sigma

    @Corr_occ.setter
    def Corr_occ(self, value):
        self.Corr_mos_occ = value

    @Corr_virt.setter
    def Corr_virt(self, value):
        self.Corr_mos_virt = value

    @Ic.setter
    def Ic(self, value):
        self.Image_charge_model = value

    @Gamma.setter
    def Gamma(self, value):
        self.Gamma_only_sigma = value
