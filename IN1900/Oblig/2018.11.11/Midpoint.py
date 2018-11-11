import numpy as np
import matplotlib.pyplot as plt

import ODESolver

class Midpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_half = u[k] + dt*f(u[k], t[k])/2
        u_new = u[k] + dt*f(u_half, t[k]+dt/2)
        return u_new

def f(x,t):
    np.cos(x)*x

T = 10
n = 15
t_points = np.linspace(0, 10, n)


solverForward = ODESolver.ForwardEuler(f)
solverForward.set_initial_condition(0)
uForward, tForward = solverForward.solve(t_points)
plt.plot(tForward, uForward, label='Forward')

solverMid = ODESolver.Midpoint(f)
solverMid.set_initial_condition(0)
uMid, tMid = solverMid.solve(t_points)

plt.plot(tMid, uMid, label='Mid')
plt.legend()
plt.show()

'''
py.exe .\Midpoint.py
Traceback (most recent call last):
  File ".\Midpoint.py", line 6, in <module>
    class Midpoint(ODESolver):
TypeError: module() takes at most 2 arguments (3 given)


'''
