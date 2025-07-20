from pycp2k.inputsection import InputSection
from ._e_density_bqb1 import _e_density_bqb1
from ._voronoi1 import _voronoi1
from ._moments1 import _moments1


class _print37(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.E_DENSITY_BQB = _e_density_bqb1()
        self.VORONOI = _voronoi1()
        self.MOMENTS = _moments1()
        self._name = "PRINT"
        self._subsections = {'E_DENSITY_BQB': 'E_DENSITY_BQB', 'VORONOI': 'VORONOI', 'MOMENTS': 'MOMENTS'}

