import numpy as np
import sys
import matplotlib.pyplot as plt
dt = float(0.01)# dt=float(sys.argv[1])
U0 = 1
T = 4
n = int(T/dt)

t = np.zeros(n+1)
u = np.zeros(n+1)

t[0] = 0
u[0] = U0

for k in range(n):
    t[k+1] = t[k] + dt
    u[k+1] = (1+dt)*u[k] # for any u[k+1]= u[k] + dt*f(u[k], t[k])


plt.plot(t,u)
plt.show()
