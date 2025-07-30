from pycp2k.inputsection import InputSection
from ._each345 import _each345


class _mo1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cartesian = None
        self.Energies = None
        self.Coefficients = None
        self.Occupation_numbers = None
        self.Occupation_numbers_stats = None
        self.Ndigits = None
        self.Mo_index_range = None
        self.EACH = _each345()
        self._name = "MO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Cartesian': 'CARTESIAN', 'Energies': 'ENERGIES', 'Coefficients': 'COEFFICIENTS', 'Occupation_numbers': 'OCCUPATION_NUMBERS', 'Occupation_numbers_stats': 'OCCUPATION_NUMBERS_STATS', 'Ndigits': 'NDIGITS', 'Mo_index_range': 'MO_INDEX_RANGE'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Eigenvalues': 'Energies', 'Eigvals': 'Energies', 'Eigenvectors': 'Coefficients', 'Eigvecs': 'Coefficients', 'Occnums': 'Occupation_numbers', 'Occnumstats': 'Occupation_numbers_stats', 'Mo_range': 'Mo_index_range', 'Range': 'Mo_index_range'}
        self._attributes = ['Section_parameters']


    @property
    def Eigenvalues(self):
        """
        See documentation for Energies
        """
        return self.Energies

    @property
    def Eigvals(self):
        """
        See documentation for Energies
        """
        return self.Energies

    @property
    def Eigenvectors(self):
        """
        See documentation for Coefficients
        """
        return self.Coefficients

    @property
    def Eigvecs(self):
        """
        See documentation for Coefficients
        """
        return self.Coefficients

    @property
    def Occnums(self):
        """
        See documentation for Occupation_numbers
        """
        return self.Occupation_numbers

    @property
    def Occnumstats(self):
        """
        See documentation for Occupation_numbers_stats
        """
        return self.Occupation_numbers_stats

    @property
    def Mo_range(self):
        """
        See documentation for Mo_index_range
        """
        return self.Mo_index_range

    @property
    def Range(self):
        """
        See documentation for Mo_index_range
        """
        return self.Mo_index_range

    @Eigenvalues.setter
    def Eigenvalues(self, value):
        self.Energies = value

    @Eigvals.setter
    def Eigvals(self, value):
        self.Energies = value

    @Eigenvectors.setter
    def Eigenvectors(self, value):
        self.Coefficients = value

    @Eigvecs.setter
    def Eigvecs(self, value):
        self.Coefficients = value

    @Occnums.setter
    def Occnums(self, value):
        self.Occupation_numbers = value

    @Occnumstats.setter
    def Occnumstats(self, value):
        self.Occupation_numbers_stats = value

    @Mo_range.setter
    def Mo_range(self, value):
        self.Mo_index_range = value

    @Range.setter
    def Range(self, value):
        self.Mo_index_range = value
