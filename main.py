import numpy as np
from solvers import solvers

def f(x):
    return np.cos(x) - x

print(solvers(1,f,1e-15))