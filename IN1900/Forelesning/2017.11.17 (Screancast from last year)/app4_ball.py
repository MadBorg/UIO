import ODESolver
import numpy as np
import matplotlib.pyplot as plt

def f(u, t):
    x, vx, y, vy = u
    g = 9.81
    return [vx, 0, vy, -g]


v0 = 5
theta = 80*np.pi/180
U0 = [0, v0*np.cos(theta), 0, v0*np.sin(theta)]
T, dt = 1.2, 0.01
n = int(round(T/dt))
solver = ODESolver.ForwardEuler(f)
solver.set_initial_condition(U0)

def terminate(u, t, step_no):
    y = u[:,2]
    return y[step_no] < 0

u, t = solver.solve(np.linspace(0, T, n+1), terminate)
x = u[:,0]
y = u[:,2]


def exact(x):
    g = 9.81
    y0 = U0[2]
    return x*np.tan(theta) - g*x**2/(2*v0**2)*1/(np.cos(theta))**2 + y0


plt.plot(x,y, 'r', x, exact(x), 'b')
plt.legend(('numerical', 'exact'))
plt.title('dt=%g' %dt)
plt.show()
