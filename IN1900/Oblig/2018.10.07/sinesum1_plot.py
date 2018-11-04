import numpy as np
import matplotlib.pyplot as plt
def f(t, T):
    if 0<t<T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2<t<T:
        return -1

def S(t, n, T):
    x = 0
    for i in range(n+1):
        x += (1/(2*i-1))*np.sin((2*(2*i-1)*np.pi*t)/T)
    return x*4/np.pi

n = [1,3,20,200]
T = 2*np.pi
t = np.linspace(0,T,1000)
fv = np.vectorize(f)
Sv = np.vectorize(S)
fvt = fv(t,T)
plt.plot(t,fvt)
for i in n:
    plt.plot(t,Sv(t,n,t))

plt.show()

'''
plotter
'''
