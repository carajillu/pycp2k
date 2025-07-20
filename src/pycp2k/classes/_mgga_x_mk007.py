from pycp2k.inputsection import InputSection


class _mgga_x_mk007(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._prefactor = None
        self._name = "MGGA_X_MK00"
        self._keywords = {'Scale': 'SCALE', '_prefactor': '_PREFACTOR'}
        self._attributes = ['Section_parameters']

