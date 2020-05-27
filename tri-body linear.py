import scipy as sp
import numpy as np
import random
from scipy import constants as C

# Mass of Argon
M_Neu = C.neutron_mass
M_Prot = C.proton_mass
M_Elec = C.electron_mass
M_Ar = 18 * (M_Elec + M_Prot) + 22 * M_Neu  # mass of argon
R = 188 * (10 ** -12)  # van der Waals radius of Ar
m = M_Ar
print(m)
# Atomic coordinates matrix
X1 = random.uniform(0, 3 * 188 * 10 ** -12)
X2 = random.uniform(0, 3 * 188 * 10 ** -12)
X3 = random.uniform(0, 3 * 188 * 10 ** -12)
alist = [X1, X2, X3]

# sorting to assign position onto data
def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            break

bubble_sort(alist)
X0 = np.array(alist)
[y1, y2, y3] = X0 #arrange values
print(X0)
# distance matrix
D1 = (y2 - y1)*10**-12
D2 = (y3 - y2)*10**-12
D3 = (3 * 188 + y1 - y3)*10**-12
D0 = np.array([D1, D2, D3]) * (10 ** -12)
# Hooke law para
RM = [R, R, R]
DX0 = D0 - RM
# spring constant
k = 3.228*10**-2  # see my research notes May the 27th Page7
# initial kinetic energy; molecular kinetic theory's conclusion,pretty rough but just fill the gap
kb = C.Boltzmann
KEi = random.uniform(kb * 1.5 * 83.81, kb * 1.5 * 87.30)
# random classical velocity generations
v1i = random.uniform(0, np.sqrt(KEi / M_Ar))
v2i = random.uniform(0, np.sqrt((KEi - 0.5 * M_Ar * v1i ** 2) / M_Ar))
v3i = ((KEi - 0.5 * M_Ar * v1i ** 2 - 0.5 * M_Ar * v2i ** 2) / M_Ar) ** 0.5
V0 = np.array([v1i, v2i, v3i])
#Starting parameters of stepwise work
dt = 10 ** -20
DX=np.array(DX0)
X=np.array(X0)
V= np.array(V0)
M=np.array([m,m,m])
A=np.array([0,0,0])
N=10
for val in range(1):
    F = -k * DX
    [f1, f2, f3] = F
    F = np.array([f3 + f2, f1 + f3, f1 + f2])
    print(F)
    A = F * (1/m)
    print(A)
    V = V + A * dt
    print(V)
    X= X+ V * dt
    print(X)
    [x1, x2, x3] = X
    bubble_sort(X)
    [x1, x2, x3] = X
    #sorting the elements of set X
    if x3< 3 * 188 * 10 ** -12:
        x3=x3
    else:x3=x3-3 * 188 * 10 ** -12
    if x2 < 3 * 188 * 10 ** -12:
        x2=x2
    else:x2 = x2 - 3 * 188 * 10 ** -12
    if x1< 3 * 188 * 10 ** -12:
        x1=x1
    else:
        x1=x1-3 * 188 * 10 ** -12
    bubble_sort([x1,x2,x3])
    X = np.array([x1,x2,x3])
    DX = np.array([x2-x1-R,x3-x2-R,3*188*10**-12+x1-x3-R])
    print(DX)


