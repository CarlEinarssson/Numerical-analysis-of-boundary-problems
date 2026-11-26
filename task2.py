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


