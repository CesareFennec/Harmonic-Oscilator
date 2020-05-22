import math
#All physical paramaters are in SIs
#systemetic parameters
k=1
m=1
dt=0.01
x0=0

#Starting paramaters
x=0
v=10
t=0
i=1
value=0
f = open ("1.txt","r+")
for i in range(1000):
        Force=-k*(x-x0)
        str(Force)
        a=Force/m
        v=v+a*dt
        x=x+v*dt
        KE=0.5*m*v**2
        P=0.5*k*(x-x0)**2
        E=KE+ P
        print(i, x, Force, v, a, KE, P, E, i*dt)
        f.write(str(E))
        f.write('\n')
#herein I wanna get some value as a string
# /so I may output the data into a txt file and reuse it for further purpose.
