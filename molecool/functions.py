"""
functions.py
A Python package for analyzing and visualizing xyz files. Fol MolSSI workshop Python Package development

Handles the primary functions
"""

#%matplotlib notebook


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is not only cool, but MOLEcoole!"
    if with_attribution:
        quote += "\n\t- Adapted from Ben Pritchard"
    return quote





if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
