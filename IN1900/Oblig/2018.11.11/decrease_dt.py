import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f,U0,t):
    import numpy as np

    n = len(t)
    u = np.zeros(n)
    u[0] = U0
    for k in range(n-1):
        dt = t[k+1] - t[k]
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

def f(x,t):
    return np.cos(6*t)/(1+t+x)


T =  10
U0 = 0
n = [20, 30, 35, 40, 50, 100, 1000, 10000]

u, t = [], []
for N in n:
    t_ = np.linspace(0,T,N)
    u_, t_ = ForwardEuler(f,U0, t_)
    u.append(u_)
    t.append(t_)
    plt.plot(t_, u_, label='n={}'.format(N))
plt.legend()
plt.show()

'''
py.exe .\decrease_dt.py

#plotter en figur

'''
