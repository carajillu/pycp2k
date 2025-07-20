from pycp2k.inputsection import InputSection
from ._gcn2 import _gcn2


class _gal211(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Metals = None
        self.Epsilon = None
        self.Bxy = None
        self.Bz = None
        self.R = None
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.A4 = None
        self.A = None
        self.B = None
        self.C = None
        self.Ah = None
        self.Bh = None
        self.Rcut = None
        self.Fit_express = None
        self.GCN = _gcn2()
        self._name = "GAL21"
        self._keywords = {'Atoms': 'ATOMS', 'Metals': 'METALS', 'Epsilon': 'EPSILON', 'Bxy': 'BXY', 'Bz': 'BZ', 'R': 'R', 'A1': 'A1', 'A2': 'A2', 'A3': 'A3', 'A4': 'A4', 'A': 'A', 'B': 'B', 'C': 'C', 'Ah': 'AH', 'Bh': 'BH', 'Rcut': 'RCUT', 'Fit_express': 'FIT_EXPRESS'}
        self._subsections = {'GCN': 'GCN'}

