from pycp2k.inputsection import InputSection


class _interaction_potential15(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Truncation_radius = None
        self.Potential_data = None
        self.Omega = None
        self.Scale_coulomb = None
        self.Scale_longrange = None
        self._name = "INTERACTION_POTENTIAL"
        self._keywords = {'Potential_type': 'POTENTIAL_TYPE', 'Truncation_radius': 'TRUNCATION_RADIUS', 'Potential_data': 'POTENTIAL_DATA', 'Omega': 'OMEGA', 'Scale_coulomb': 'SCALE_COULOMB', 'Scale_longrange': 'SCALE_LONGRANGE'}
        self._aliases = {'Cutoff_radius': 'Truncation_radius', 'Tshpsc_data': 'Potential_data', 'T_c_g_data': 'Potential_data'}


    @property
    def Cutoff_radius(self):
        """
        See documentation for Truncation_radius
        """
        return self.Truncation_radius

    @property
    def Tshpsc_data(self):
        """
        See documentation for Potential_data
        """
        return self.Potential_data

    @property
    def T_c_g_data(self):
        """
        See documentation for Potential_data
        """
        return self.Potential_data

    @Cutoff_radius.setter
    def Cutoff_radius(self, value):
        self.Truncation_radius = value

    @Tshpsc_data.setter
    def Tshpsc_data(self, value):
        self.Potential_data = value

    @T_c_g_data.setter
    def T_c_g_data(self, value):
        self.Potential_data = value
