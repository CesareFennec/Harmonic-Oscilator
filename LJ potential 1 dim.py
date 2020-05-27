import numpy as np
from scipy import constants as C
from matplotlib import pyplot as plt
import random as ran
d=188*10**-12
M=6.69719964739627e-26
kb=C.Boltzmann
emma=kb*118.2
print(emma)
sigma=341.9
a=100/sigma
b=400/sigma
r=np.arange(a,b,1000)
P=4*(-r**-6+r**-12)
plt.title('LJ potential of Argon for ref 1')
plt.plot(r,P)
plt.show()
plt.savefig("1d LJP.PNG")