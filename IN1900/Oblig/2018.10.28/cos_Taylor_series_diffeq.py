import math as m
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4*np.pi,1000)
n_list = [1,2,3,6,12]
def S(x,n):
    data = 0
    for j in range(0,n+1):
        data  = data + (((-1)**j)* (x**(2*j))/(m.factorial(2*j)))
    return data

for n in n_list:
    plt.plot(x,S(x,n), label='n = {}'.format(n))

plt.plot(x,np.cos(x),label='sin(x)', linewidth=2)
plt.ylim([-1.5,1.5])

plt.legend()
plt.show()
'''
python plot_Taylor_sin.py

#plotter figure1 som er taylorplottet
'''
