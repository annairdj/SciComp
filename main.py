import numpy as np
from solvers import solvers
from scipy import optimize

def f(x):
    return np.cos(x)-x

print(solvers(1,f,1e-5))

sols = optimize.root(f, 0)
print(sols.x)