"""
molecool
A Python package for analyzing and visualizing xyz files. Fol MolSSI workshop Python Package development
"""

# Add imports here
from .atom_data import atomic_weights, atom_colors
from .functions import *
from .measure import calculate_angle, calculate_distance
from .molecule import *
from .visualize import draw_molecule, draw_bond_histogram
from .io import xyz, pdb

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
