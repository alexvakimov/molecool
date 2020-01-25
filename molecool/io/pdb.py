"""
pdb.py

Read and write the PDB files
"""
import numpy as np

def open_pdb(file_location):
    """
    This function reads in a pdb file and returns the atom names and coordinates.

    Parameters
    ----------
    file_location : string
        The name of the PDB file to read
        
    Returns
    -------
        symbols : list of strings
            The atomic symbols
        coordinates : np.ndarray
            The coordinates from the pdb file

    Examples
    --------
    >>> sym, coords = open_pdb("water.pdb")
    ["H", "H", "O"], [...]

    """
    
    
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)

    # Converts list to numpy array
    coordinates = np.array(coordinates)

    return symbols, coordinates

