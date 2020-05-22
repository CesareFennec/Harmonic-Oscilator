import numpy as np
#here we use analytical solution to describe a harmonic oscillator

#parameters
k = 1
m = 1
A = 2
Omega = (k/m)**0.5

#INPUT TIME
t = 6

#input initial phase
Psi0 = 0

#Dynamic Functions
x = A * np.cos(Omega*t + Psi0)
v = A * Omega * np.sin(Omega*t + Psi0)

#time parameters
Period = 2 * np.pi / Omega
T      = Period
mu     = 1 / T

#energy parameters
KE = 0.5 * m * v **2 #kinetic energy of the ball
P  = 0.5 * k * x **2#potential energy of the spring
E  = P + KE#total energy

#output
print(x,v,T,mu, KE,P,E)