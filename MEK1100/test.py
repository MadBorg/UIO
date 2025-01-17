def streamfun(n=20):
    import numpy as np
    '''Regner ut et grid og en strømfunksjon'''

    x=np.linspace(-0.5*np.pi,0.5*np.pi,n)
    #resultatet er en vektor med n elementer, fra -pi/2 til pi/2
    [X,Y] = np.meshgrid(x,x)
    psi=np.cos(X)*np.cos(Y)

    return X, Y, psi

import matplotlib.pyplot as plt

x,y,psi = streamfun(input("n = "))
plt.contour(x,y,psi)
plt.show()
