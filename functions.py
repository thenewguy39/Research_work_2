import math 
import numpy as np
class Tools:

    def __init__(self):
        pass

    def tabulate(x, y, f):
        """Return a table of f(x, y). Useful for the Gram-like operations."""
        return np.vectorize(f)(*np.meshgrid(x, y, sparse=True))

    def cos_sum(a, b):
        """To work with tabulate."""
        return(math.cos(a+b))