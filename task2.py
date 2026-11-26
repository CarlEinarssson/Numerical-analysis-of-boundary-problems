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


def FDMd2dx2 (L , BCleft , BCright , N = 100)
    if BCleft is Dirichlet:
        BCleft_value = BCleft.value
    if BCright is Dirichlet:
        BCright_value = BCright.value
    if BCleft is Neumann:
        BCleft_derivative = BCleft.value
    if BCright is Neumann:
        BCright_derivative = BCright.value
    
    dx = L / (N - 1)
    grid = np.linspace(0, L, N)
    A = np.zeros((N, N))
    BCcorr = np.zeros(N)




