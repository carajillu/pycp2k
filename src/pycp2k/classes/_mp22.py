from pycp2k.inputsection import InputSection


class _mp22(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Method = None
        self.Big_send = None
        self._name = "MP2"
        self._keywords = {'Method': 'METHOD', 'Big_send': 'BIG_SEND'}
        self._attributes = ['Section_parameters']

