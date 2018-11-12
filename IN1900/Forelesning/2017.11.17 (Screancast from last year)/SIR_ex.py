import numpy as np
import matplotlib.pyplot as plt
dt = 0.1
D = 30
N = int(D*24/dt)
beta, nu, = 0.0013, 0.008333

t = np.linspace(0, N*dt, N+1)
S = np.zeros(N+1)
I = np.zeros(N+1)
R = np.zeros(N+1)
S[0] = 50
I[0] = 1

for n in range(N):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*nu*I[n]
    R[n+1] = R[n] + dt*nu*I[n]

plt.plot(t, S, 'k-', t, I, 'b-', t, R, 'r-')
plt.legend(['S', 'I', 'R'], loc = 'lower right')
plt.xlabel('hours')
plt.show()
