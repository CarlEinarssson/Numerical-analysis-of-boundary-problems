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
    if BCleft is Dirichlet:
        BCleft_value = BCleft.value
    if BCright is Dirichlet:
        BCright_value = BCright.value
    if BCleft is Neumann:
        BCleft_derivative = BCleft.value
    if BCright is Neumann:
        BCright_derivative = BCright.value
    
    dx = L / (N + 1)
    grid = np.linspace(0, L, N+1)

    BCcorr = np.zeros(N)
    BCcorr[0] = BCleft_value/ dx**2
    BCcorr[N-1] = BCright_value/ dx**2

    c = np.zeros(N)
    c[0] = -2
    if N > 1:
        c[1] = 1
    A = sp.linalg.toeplitz(c, c) / dx**2



