from Oppg2c import *

import numpy as np
import matplotlib.pyplot as plt

def lin_pendel(t, v0, theta0, g, L):
    return theta0 * np.cos(np.sqrt(g/L)*t) + v0/np.sqrt(g*L) * np.sin(np.sqrt(g/L)*t)

g, L, v0, theta0 = 9.81, 1, 0, np.pi/2
N = [2**5, 2**10]
T = 4
h = [T/n for n in N]
t = [np.linspace(0,T,n+1) for n in N]


if __name__ == "__main__":
    plt.subplot(2, 1, 1)
    v_hat, theta_hat = lin_pendel_euler(v0, theta0, g, L, N[0], h[0])
    theta = lin_pendel(t[0], v0, theta0, g, L)
    plt.plot(t[0], theta, label='ϴ exact')
    plt.plot(t[0], theta_hat, label='ϴ estimate, N ={}'.format(N[0]))
    plt.legend()

    plt.subplot(2, 1, 2)
    v_hat, theta_hat = lin_pendel_euler(v0, theta0, g, L, N[1], h[1])
    theta = lin_pendel(t[1], v0, theta0, g, L)
    plt.plot(t[1], theta, label='ϴ exact')
    plt.plot(t[1], theta_hat, label='ϴ estimate, N ={}'.format(N[1]))
    plt.legend()

    plt.show()
