from pycp2k.inputsection import InputSection


class _excited_states1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.State = None
        self.Xc_kernel_method = None
        self._name = "EXCITED_STATES"
        self._keywords = {'State': 'STATE', 'Xc_kernel_method': 'XC_KERNEL_METHOD'}
        self._attributes = ['Section_parameters']

