from pycp2k.inputsection import InputSection


class _tip_scan1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scan_direction = None
        self.Reference_point = None
        self.Scan_points = None
        self.Scan_step = None
        self.Tip_filename = None
        self._name = "TIP_SCAN"
        self._keywords = {'Scan_direction': 'SCAN_DIRECTION', 'Reference_point': 'REFERENCE_POINT', 'Scan_points': 'SCAN_POINTS', 'Scan_step': 'SCAN_STEP', 'Tip_filename': 'TIP_FILENAME'}
        self._attributes = ['Section_parameters']

