def streamfun(n=20):
    import numpy as np
    '''Regner ut et grid og en strømfunksjon'''

    x=np.linspace(-0.5*np.pi,0.5*np.pi,n)
    #resultatet er en vektor med n elementer, fra -pi/2 til pi/2
    [X,Y] = np.meshgrid(x,x)
    psi=np.cos(X)*np.cos(Y)

    return X, Y, psi

import matplotlib.pyplot as plt
plt.figure()
plt.title("n = 5")
x,y,psi = streamfun(5)
a = plt.contour(x,y,psi, colors = "red", label ="5")

plt.figure()
plt.title("n = 30")
x,y,psi = streamfun(30)
b = plt.contour(x,y,psi, colors ="blue", text = "30")

plt.legend()
plt.show()
