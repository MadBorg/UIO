import matplotlib.pyplot as plt
import numpy as np

def ForwardEuler(f,U0, T, n):

    import numpy as np
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t


def f(u, t):
    return t - 2*t*u

U0 = 1
T = 4
n = int(1e6)



u, t = ForwardEuler(f, U0, T, n)

plt.plot(t,u,t, np.exp(-t**2) + 1/2)
plt.show()
