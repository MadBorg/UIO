from Oppg2c import *
from Oppg2d import *

import numpy as np
import matplotlib.pyplot as plt



class epsilon:
    def __init__(self,f, f_hat,v0, theta0, g, L, T):
        self.f = f
        self.f_hat = f_hat
        self.v0, self.theta0, self.L= v0, theta0, L
        self.T = T

    def __call__(self, h, N):
        v0, theta0, L = self.v0, self.theta0, self.L
        T = self.T
        t = np.linspace(0,T,int(N+1))
        f = self.f(t, v0, theta0, g, L)
        f_hat = self.f_hat(v0, theta0, g, L, N, h)[1]
        return abs(f[-1]-f_hat[-1])
if __name__ == "__main__":
    N = [2**i for i in range(4,11)]
    T = 4
    h = [T/n for n in N]
    g, L, v0, theta0 = 9.81, 1, 0, np.pi/2

    print('''-------------------------
|   N        h     e(p) |''')
    for i in range(len(N)):
        e = epsilon(lin_pendel,lin_pendel_euler,v0, theta0, g, L, T)
        print('|{:.2e} {:.4f} {:7.4f}|'.format(N[i], h[i], e(h[i], N[i]) ))
