import numpy as np
import matplotlib.pyplot as plt

def lin_pendel_euler(v0, theta0, g, L, N, h):
    v, theta = [0]*(N+1), [0]*(N+1)
    v[0], theta[0] = v0, theta0

    for k in range(N):
        v[k+1] = v[k] - g*h*theta[k]
        theta[k+1] = theta[k] + h*(v[k]/L)
    return v, theta


g, L, v0, theta0, T, N = 9.81, 1, 0, np.pi/2, 4, 2**20
h = T/N

v, theta = lin_pendel_euler(v0, theta0, g, L, N, h)

'''
for i, j in zip(v, theta):
    print(i,j)
'''
plt.plot(theta, v)
plt.show()
