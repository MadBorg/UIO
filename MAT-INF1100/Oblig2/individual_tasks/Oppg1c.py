from Oppg1a import *
from Oppg1b import *

import numpy as np
import matplotlib.pyplot as plt
t = []
v = []
infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()

V = np.asarray(avstand(t, v))
dv = np.asarray(aksellerasjon(t, v))
if __name__ == "__main__":
    plt.subplot(211)
    plt.plot(t[1:],dv,label='aksellerasjon')
    plt.xlabel('tid'); plt.ylabel('aksellerasjon')
    plt.legend()

    plt.subplot(212)
    plt.plot(t, V, label='avstand')
    plt.xlabel('tid'); plt.ylabel('avstand')
    plt.legend()

    plt.show()
