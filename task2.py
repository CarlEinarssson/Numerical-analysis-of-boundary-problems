import numpy as np
import scipy as sp
import scipy . linalg
import matplotlib.pyplot as plt

class BC(object):
    def __init__ (self, value):
        self.value = value

class Dirichlet(BC):
    def __init__(self, value):
        BC.__init__(self, value)

class Neumann(BC):
    def __init__(self, value):
        BC.__init__(self, value)


def FDMd2dx2 (L , BCleft , BCright , N = 100):    
    dx = L / (N + 1)
    grid = np.linspace(0, L, N + 2)[1:-1]
    BCcorr = np.zeros(N)
    
    c = np.zeros(N)
    c[0] = -2
    if N > 1:
        c[1] = 1
    A = sp.linalg.toeplitz(c, c) / dx**2
    
    if isinstance(BCleft, Dirichlet):
        BCcorr[0] = BCleft.value / dx**2
    elif isinstance(BCleft, Neumann):
        A[0, 0] = -2 / dx**2
        A[0, 1] = 2 / dx**2
        BCcorr[0] = -2 * BCleft.value / dx
    
    if isinstance(BCright, Dirichlet):
        BCcorr[-1] = BCright.value / dx**2
    elif isinstance(BCright, Neumann):
        A[-1, -1] = -2 / dx**2
        A[-1, -2] = 2 / dx**2
        BCcorr[-1] = 2 * BCright.value / dx
        
    return dx, grid, A, BCcorr



