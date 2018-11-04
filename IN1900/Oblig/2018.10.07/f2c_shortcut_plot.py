
import matplotlib.pyplot as plt
import numpy as np
def f2c_simple(f):
    return (f-30)/2

def f2c_exact(f):
    return (f-32)*5/9

f = np.linspace(-20,120,1e4)
c_simple, c_exact = f2c_simple(f), f2c_exact(f)

plt.plot(f,c_simple ,'g',label='f2c_simple')
plt.plot(f,c_exact ,'m',label='f2c_exact')
plt.legend()
plt.show()
'''
Terminal python f2c_shortcut_plot.py
#plotter Figure 1

'''
