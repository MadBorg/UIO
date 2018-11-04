import numpy as np
import matplotlib.pyplot as plt


L, N, p = 100, 360, 5 

index_set = range(N+1)
x = np.zeros(len(index_set))
y = np.zeros_like(x)#np.zeros(len(index_set))

x[0], y[0] = L, 0

for n in index_set[1:]:
    y[n] = x[n-1]*p/(12*100) + L/N
    x[n] = x[n-1] + x[n-1]*p/(12*100)-y[n]

#plt.plot(x,'ro')
plt.plot(y, 'b+')
plt.show()
