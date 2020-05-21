import numpy as np
#here we use analytical solution to describe a harmonic oscillator

#parameters
k = 1
m = 1
Omega = (k/m)**0.5

#INPUT TIME
t = 6

#input initial positions
Psi0 = 0

#Dynamic Func
x = np.cos(Omega*t + Psi0)
v = Omega * np.sin(Omega*t + Psi0)

#otherparameters
Period = 2 * np.pi / Omega
T = Period

#output
print(x,v,T)