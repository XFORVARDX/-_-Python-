import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.colors import LightSource
import sys
import time 
import random
# Make the X, Y meshgrid.
def my_spher(N = 20, R=2):
  # parametric
  u = np.linspace(0, 2 * np.pi, N)
  v = np.linspace(0, np.pi, N)
  x = R * np.outer(np.cos(u), np.sin(v))
  y = R * np.outer(np.sin(u), np.sin(v))
  z = R * np.outer(np.ones(np.size(u)), np.cos(v))
  return x,y,z
X,Y,Z = my_spher()

alf=random.randrange(360)
v=10

