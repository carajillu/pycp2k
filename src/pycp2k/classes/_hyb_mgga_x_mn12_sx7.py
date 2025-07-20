from pycp2k.inputsection import InputSection


class _hyb_mgga_x_mn12_sx7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cc000 = None
        self._cc001 = None
        self._cc002 = None
        self._cc003 = None
        self._cc004 = None
        self._cc005 = None
        self._cc010 = None
        self._cc011 = None
        self._cc012 = None
        self._cc013 = None
        self._cc014 = None
        self._cc020 = None
        self._cc021 = None
        self._cc022 = None
        self._cc023 = None
        self._cc030 = None
        self._cc031 = None
        self._cc032 = None
        self._cc100 = None
        self._cc101 = None
        self._cc102 = None
        self._cc103 = None
        self._cc104 = None
        self._cc110 = None
        self._cc111 = None
        self._cc112 = None
        self._cc113 = None
        self._cc120 = None
        self._cc121 = None
        self._cc122 = None
        self._cc200 = None
        self._cc201 = None
        self._cc202 = None
        self._cc203 = None
        self._cc210 = None
        self._cc211 = None
        self._cc212 = None
        self._cc300 = None
        self._cc301 = None
        self._cc302 = None
        self._ax = None
        self._sx = None
        self._omega = None
        self._name = "HYB_MGGA_X_MN12_SX"
        self._keywords = {'Scale': 'SCALE', '_cc000': '_CC000', '_cc001': '_CC001', '_cc002': '_CC002', '_cc003': '_CC003', '_cc004': '_CC004', '_cc005': '_CC005', '_cc010': '_CC010', '_cc011': '_CC011', '_cc012': '_CC012', '_cc013': '_CC013', '_cc014': '_CC014', '_cc020': '_CC020', '_cc021': '_CC021', '_cc022': '_CC022', '_cc023': '_CC023', '_cc030': '_CC030', '_cc031': '_CC031', '_cc032': '_CC032', '_cc100': '_CC100', '_cc101': '_CC101', '_cc102': '_CC102', '_cc103': '_CC103', '_cc104': '_CC104', '_cc110': '_CC110', '_cc111': '_CC111', '_cc112': '_CC112', '_cc113': '_CC113', '_cc120': '_CC120', '_cc121': '_CC121', '_cc122': '_CC122', '_cc200': '_CC200', '_cc201': '_CC201', '_cc202': '_CC202', '_cc203': '_CC203', '_cc210': '_CC210', '_cc211': '_CC211', '_cc212': '_CC212', '_cc300': '_CC300', '_cc301': '_CC301', '_cc302': '_CC302', '_ax': '_AX', '_sx': '_SX', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

