import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
N = 500
qmax = 5
qmin = -qmax #Psi(q) func in Dirac Func
dq = (qmax-qmin)/(N-1)
epi = 0.5/dq/dq
M = np.zeros((N, N)) #get N-dim square matrix
U = np.zeros(N) #N-dim column
q = np.zeros(N) #N-dim column as well for value of Psi(q)
for val in range(0, N):
    q[val] = qmin+dq*val
    U[val] = 0.5*q[val]*q[val] #stepwise calc of Psi(q)
M[0][0]=2*epi+U[0] #define for first several Elemants
M[0][1]=-epi
for val in range(1, N-1):
    M[val][val-1]=-epi
    M[val][val]=2*epi+U[val]
    M[val][val+1]=-epi
M[N-1][N-2]=-epi
M[N-1][N-1]=2*epi+U[N-1] #construct a prob density matrix

eg , vt=la.eig(M) #to calc prob of specific position
print(eg)  #
for val in range (0,N):
    q[val] = qmin + dq * val
    print(val,q[val],vt.T[0,val],vt.T[1,val],vt.T[2,val],vt.T[3,val],vt.T[4,val])