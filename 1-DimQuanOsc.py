#QuantumOscillator
import numpy as np
import scipy as scp
from scipy import constants as C
import matplotlib.pyplot as plt
#nota bonne all units are in
#Define elastic constant
k = 1
m1 = 1
m2 = 1
pi= np.pi
hbar=C.hbar
m = m1*m2/(m1+m2) #reduced mass
Omega = (k/m)**.5
for q in range(0,5):
    E =hbar*Omega*(q +0.5) #Eigenvalue
    print(q,E)
