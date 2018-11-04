'''
.
.
.
'''
import numpy as np
import matplotlib.pyplot as plt
def D(f,x,N):
    index_set = range(N+1)
    d = np.zeros(len(index_set))

    for n in index_set:
        h = 2**(-n)
        d[n] = (f(x+h)-f(x))/h

    return d

d1 = D(np.sin,0,80)

plt.plot(d1, 'o', fillstyle='none')
plt.show()
