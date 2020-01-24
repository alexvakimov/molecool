"""
molecool
A Python package for analyzing and visualizing xyz files. Fol MolSSI workshop Python Package development
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
