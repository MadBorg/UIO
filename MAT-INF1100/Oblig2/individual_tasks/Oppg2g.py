from Oppg2f import *

import matplotlib.pyplot as plt
import numpy as np

def pendel_euler(v0, theta0, g, L, N, h):
    v = np.zeros(N+1)
    theta = np.zeros(N+1)
    v[0], theta[0] = v0, theta0
    for k in range(N):
        v[k+1] = v[k] - g*np.sin(theta[k])*h
        theta[k+1] = theta[k] + h* (1/L * v[k])
    return v, theta


g, L, v0, theta0 = 9.81, 1, 0, np.pi/2
T = 4
N = 2**5
h = T/N
t = np.linspace(0,T,N+1)

v_pendel_euler, theta_pendel_euler = pendel_euler(v0, theta0, g, L, N, h)
theta_lin_pendel = lin_pendel(t, v0, theta0, g, L)
v_lin_pendel_euler, theta_lin_pendel_euler = lin_pendel_euler(v0, theta0, g, L, N, h)

plt.plot(t,theta_pendel_euler, label='theta_pendel_euler')
plt.plot(t,theta_lin_pendel, label='theta_lin_pendel')
plt.plot(t,theta_lin_pendel_euler, label='theta_lin_pendel_euler')
plt.xlabel('time: t')
plt.ylabel('theta')
plt.legend(title ='N = 2**5')
plt.show()
