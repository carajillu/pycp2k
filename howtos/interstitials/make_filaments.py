import ase as ase
from ase import Atoms, Atom
from copy import deepcopy
import numpy as np
import os

from ase.io import read, write
atoms = read("HfO2_supercell.pdb", index=0)

def make_surface(atoms: Atoms, vacuum: float = 10.0) -> Atoms:
    """
    Create a surface from the given atoms with a specified vacuum.
    """
    from ase import build
    slab = build.surface(atoms, (1, 1, 1), vacuum=vacuum, layers=3)
    return slab

def make_interstitial(atoms: Atoms, vac_index: int, direction:list=[0,0,1])-> Atoms:
    """
    Create an interstitial atom at the specified position.
    """
    position = atoms.get_positions()[vac_index]
    interstitial_atom = Atom('O', position=position + np.array([direction[0], direction[1], direction[2]]))
    atoms.append(interstitial_atom)
    print(len(atoms))
    atoms.set_distance(vac_index, -1, distance=2.5, fix=0.5, mic=True)
    return atoms

def find_cylinders(temp: Atoms, diameter: float)-> list:
    """delete atoms in a cylinder around the center of the cell"""
    cell_center = temp.cell.sum(axis=0) / 2
    print("Cell center:", cell_center)
    vacs_index = []
    for cylinder in [diameter]:
        new_vacs = 0
        for atom in temp:
            if atom.symbol == "O":
                dist = atom.position - cell_center
                if np.linalg.norm(dist[0]**2 + dist[1]**2) < cylinder:
                    new_vacs += 1
                    vacs_index.append(atom.index)
    return vacs_index

def find_neighbours(temp: Atoms, center=[0,0,0], diameter=2.0)-> list:
    """delete atoms in a cylinder around the center of the cell"""
    cell_center = center
    print("Cell center:", cell_center)
    vacs_index = []
    for cylinder in [diameter]:
        print("Cylinder diameter:", cylinder)
        new_vacs = 0
        for atom in temp:
            if atom.symbol == "O":
                dist = atom.position - cell_center
                print("Distance from center:", dist, np.linalg.norm(dist))
                if np.linalg.norm(dist) < cylinder:
                    new_vacs += 1
                    vacs_index.append(atom.index)
    return vacs_index