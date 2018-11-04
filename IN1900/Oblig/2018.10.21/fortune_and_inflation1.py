import numpy as np
import matplotlib.pyplot as plt
def loan(L,N, p):
    x,y = np.zeros(N+1), np.zeros(N+1);
    x[0] = L
    for n in range(1,N+1):
        y[n] = (p/(12*100)) *x[n-1] + L/N
        x[n]= x[n-1] + (p/(12*100))*x[n-1] - y[n]
    return x,y



L = 1e6 #
N = 100
p = 5

x,y = loan(L,N, p)
#print('{}\n\n{}'.format(x,y))

plt.plot(list(range(N+1)), x)
#plt.plot(list(range(1,N+1)), [1:])
plt.show()

'''
python fortune_and_inflation1.py

#plotter figure1 som er Xn
'''
