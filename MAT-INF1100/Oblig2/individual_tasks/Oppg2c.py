import numpy as np
import matplotlib.pyplot as plt

def lin_pendel_euler(v0, theta0, g, L, N, h=1e-14):
    T = h*N #siden vi har h = T/N
    v, theta = [0]*(N+1), [0]*(N+1)
    v[0], theta[0] = v0, theta0

    for k in range(N):
        v[k+1] = v[k] - g*h*theta[k]
        theta[k+1] = theta[k] + h*(v[k]/L)
    return v, theta
