import numpy as np
import matplotlib.pyplot as plt
def RungeKutta2_func(f, u0, T, n):
    
    u = np.zeros(N)
    dt = np.zeros(N)

    for k in range(1, N-1):
        dt[k] = t[k] - t[k-1]
        K1 = dt[k]+f(u[k], t[k])
        K2 = dt[k]+f(u[k] + 1/2*K1, t[k] + 1/2 * dt[k])
        u[k+1] = u[k] + K2
    return u



def f(u, t):
    return np.sin(u)#*1.02*g(t)

def g(t):
    return t

t = np.linspace(0,4, 100)

y = RungeKutta2_func(f,t)

plt.plot(t,y)
plt.show()
