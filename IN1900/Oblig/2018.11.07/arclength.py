import numpy as np
import matplotlib.pyplot as plt

def integral(g, a, b, N=20):
    index_set = range(N+1)
    x = np.linspace(a,b,N+1)
    g_ = np.zeros_like(x)
    f_ = np.zeros_like(x)
    g_[0] = g(x[0])
    f_[0] = 0

    for n in index_set[1:]:
        g_[n] = g(x[n])
        f_[n] = f_[n-1] + 0.5*(x[n] - x[n-1])*(g_[n-1] + g_[n])
    return x, f_

def g(t):
    return np.sqrt(1+(derivative(f,t)))

def f(x):
    g = lambda t : 1/np.sqrt(2*np.pi)*np.exp(-4*t**2)
    return integral(g,-2, x)

def derivative(f, x, h=1e-14):
    return (f(x+h) - f(x))/h

def arclength(f, a, b, n):
    g = lambda t: np.sqrt(1+(derivative(f,t)))
    x,s = integral(g,a,b,n)
    return x,s

x,s = arclength(f,-2,2,10000)
plt.plot(x,s)
plt.show()
