import numpy as np
import matplotlib.pyplot as plt
import scipy

def solvers(x0, f, e):
    x = x0
    h = 1e-5
    while np.abs(f(x)) >= e:
        x -= h*f(x)/(f(x+h)-f(x))
    return x
