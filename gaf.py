import math
import numpy as np
from functions import Tools

class GAF: 
    def __init__(self):
        pass

    def transform(serie):
        """Compute the Gramian Angular Field of an image"""
        # # Min-Max scaling
        # min_ = np.amin(serie)
        # max_ = np.amax(serie)
        # scaled_serie = (2*serie - max_ - min_)/(max_ - min_)

        # Floating point inaccuracy!
        serie = np.where(serie >= 1., 1., serie)
        serie = np.where(serie <= -1., -1.,serie)

        # Polar encoding
        phi = np.arccos(serie)
        # Note! The computation of r is not necessary
        r = np.linspace(0, 1, len(serie))

        # GAF Computation (every term of the matrix)
        gaf = Tools.tabulate(phi, phi, Tools.cos_sum)

        return gaf