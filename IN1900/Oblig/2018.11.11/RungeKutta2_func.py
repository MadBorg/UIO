import numpy as np
import matplotlib.pyplot as plt

def RungeKutta2_func(f, u0, t):
    import numpy as np
    n = len(t)
    u = np.zeros(n)
    u[0] = U0

    for k in range(n-1):
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + K1/2, t[k] + 1/2 * dt)
        u[k+1] = u[k] + K2
    return u

def f(u,t):
    return u

U0, T =1, 5

N = [5,10,20,100]
t, u, y = [],[],[]

for n in N:
    t.append(np.linspace(0,T,n))
    u.append(RungeKutta2_func(f, U0, t[-1]))
    y.append(np.exp(t[-1]))

diff = [i-j for i,j in zip(u,y)]

plt.subplot(2,1,1)
for i,j,n in zip(t,u,N):
    plt.plot(i,j, label='n={}'.format(n))
plt.plot(t[-1], y[-1])
plt.legend()

plt.subplot(2,1,2)
for i,j,n in zip(t, diff, N):
    plt.plot(i,j, label='n={}'.format(n))
plt.legend()

plt.show()

'''
siden dt er mindre når n, og når n øker så ser vi på plottet at erroren blir mindre. Vist i subplot 2

python .\RungeKutta2_func.py

to plots, 1. er estimatet, 2. er errorena
'''
