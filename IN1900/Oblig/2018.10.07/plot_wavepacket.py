import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
    return np.exp(-(x-3*t)**2) * np.sin(3*np.pi*(x-t))

n = 1e4
x = np.linspace(-4,4, n)
t = 0
f_array = f(x,t)
plt.plot(x,f_array)
plt.show()

'''
Terminal python plot_wavepacket.py
#plotter Figure 1

'''
