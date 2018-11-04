import numpy as np
import matplotlib.pyplot as plt
def c(l,g=9.81, s=7.9e-2, rho=1e4, h=50):
    return np.sqrt((g*l)/(2*np.pi) * (1 + s*(4*np.pi)/(rho*g*l))*np.tanh((2*np.pi*h)/l))


n = 1e4
smal_l = np.linspace(1e-3,0.1, n)
big_l = np.linspace(1,1e4, n)


plt.subplot(211)
plt.plot(smal_l, c(smal_l), label ='C_smal')
plt.subplot(212)
plt.plot(big_l, c(big_l),label ='C_big')
plt.show()

'''
Terminal python water_wave_velocity.py
#plotter Figure 1, med to subplot

'''
