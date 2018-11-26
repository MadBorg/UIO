from Oppg2c import *
from Oppg2d import *
from Oppg2e import *

import numpy as np
import matplotlib.pyplot as plt


class konvergens(epsilon):
    def p(self, h1, N):
        e = self.__call__
        h2 = h1/2
        return np.log(e(h1, N)/e(h2, N*2))/np.log(h1/h2)


if __name__ == "__main__":
        N = [2**i for i in range(4,11)]
        T = 4
        h = [T/n for n in N]

        print('''-----------------------------------
|    N        h      e(p)     p   |''')
        for i in range(len(N)):
            e = konvergens(lin_pendel,lin_pendel_euler,v0, theta0, g, L, T)
            p = e.p(h[i], N[i])
            print('| {:.2e}{:8.4f}{:8.4f}{:8.4f}|'.format(N[i], h[i], e(h[i], N[i]), p))
