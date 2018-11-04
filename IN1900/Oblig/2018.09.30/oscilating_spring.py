import numpy as np
import matplotlib.pyplot as plt

def y(t, A, gamma, k, m):
    return A * np.exp(-gamma*t)*np.cos(np.sqrt(k/m)*t)

A, gamma, k, m = 0.3, 0.15,4, 9
n, start, stop = 101, 0, 25

interval = np.linspace(start,stop,n)
t_array = np.zeros(n)
y_array = np.zeros(n)

for i in range(len(interval)):
    t_array[i] = interval[i]
    y_array[i] =  y(interval[i], A, gamma, k, m)
#t_array = np.linspace(start,stop,n)
#y_array = y(t_array, A, gamma, k, m)
#for i,j in zip(t_array,y_array):
#    print(i, j)
#b
t_array2 = np.linspace(start,stop,n)
y_array2 = y(t_array, A, gamma, k, m)
#c
plt.plot(t_array,y_array)
plt.plot(t_array2, y_array2)
plt.show()
