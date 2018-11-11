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

class Logistic:
    def __init__(self, alpha, R, U0):
        self.alpha, self.R, self.U0 = alpha, R, U0

    def __call__(self, u, t):
        return self.alpha * u * (1-u/self.R)



U0 = 1
T = 10
n = int(1e5)

f = Logistic(1.1, 100, 0)

u, t = ForwardEuler(f, U0, T, n)

plt.plot(t,u)
plt.show()
