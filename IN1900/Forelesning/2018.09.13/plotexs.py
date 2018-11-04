import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 10, 0.1)


def f(x):
    y = np.sin(x)
    return y


def der(x, f, h=1e-1):
    return (f(x+h) - f(x-h))/(2*h)


plt.plot(x, f(x))
plt.plot(x, der(x, f))
plt.plot(x, np.cos(x))
plt.show()
