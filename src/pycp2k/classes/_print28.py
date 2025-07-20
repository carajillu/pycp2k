from pycp2k.inputsection import InputSection


class _print28(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NO_DEFAULT = None
        self._name = "PRINT"
        self._keywords = {'NO_DEFAULT': None}
        self._aliases = {'Self_energy': 'NO_DEFAULT'}


    @property
    def Self_energy(self):
        """
        See documentation for NO_DEFAULT
        """
        return self.NO_DEFAULT

    @Self_energy.setter
    def Self_energy(self, value):
        self.NO_DEFAULT = value
