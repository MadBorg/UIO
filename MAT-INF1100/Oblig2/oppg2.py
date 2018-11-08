import numpy as np
import matplotlib.pyplot as plt
#c)

def lin_pendel_euler(v0, theta0, g, L, N, T, h=None):
    if h is None:
        h = T/N
    v, theta = [0]*(N+1), [0]*(N+1)
    v[0], theta[0] = v0, theta0

    for k in range(N):
        v[k+1] = v[k] - g*h*theta[k]
        theta[k+1] = theta[k] + h*(v[k]/L)
    return v, theta



#d)
def lin_pendel(t, v0, theta0, g, L):
    return theta0 * np.cos(np.sqrt(g/L)*t) + v0 * np.sin(np.sqrt(g/L)*t)

g, L, v0, theta0, T, N1 = 9.81, 1, 0, np.pi/2, 4, 2**5
v_hat, theta_hat = lin_pendel_euler(v0, theta0, g, L, N1, T)

t1 = np.linspace(0,T,N1+1) #[h*k for k in range(N)]
theta1 = lin_pendel(t1, v0, theta0, g, L)

plt.subplot(2, 1, 1)
plt.plot(t1,theta1, label='ϴ exact')
plt.plot(t1,theta_hat, label='ϴ estimate, N =2*5')
plt.legend()

plt.subplot(2, 1, 2)
N2 = 2**10
v_hat, theta_hat = lin_pendel_euler(v0, theta0, g, L, N2, T)
t2 = np.linspace(0,T,N2+1) #[h*k for k in range(N)]
theta2 = lin_pendel(t2, v0, theta0, g, L)

plt.plot(t2,theta2, label='ϴ exact')
plt.plot(t2,theta_hat, label='ϴ estimate, N = 2**10')
plt.legend()

plt.show()


#e)

def epsilon(N, h=None):
    t = np.linspace(0,T,N+1)
    theta = lin_pendel(t, v0, theta0, g, L)
    theta_hat = np.asarray(lin_pendel_euler(v0, theta0, g, L, N, T, h)[-1])
    err = np.absolute(theta-theta_hat)
    return err

n = [2**i for i in range(4,10+1)]

for N in n:
    err = epsilon(2**10)
    print('''---------------
    N = {}'''.format(N))
    for i in range(1, len(err), int(len(err)/10)):
        print('err[{}] = {}'.format(i, err[i]))


#f)

def p(epsilon):
    N = 2**4
    h2 = (T/N)/2
    h1 = T/N
    return (np.log(epsilon(N)/epsilon(N)))/np.log(h1/h2)


print(p(epsilon))

#g
def pendel_euler(v0, theta0, g, L, N, h):
    v = theta =np.zeros(N+1)
    v[0], theta[0] = v0, theta0
    for k in range(N):
        v[k+1] = v[k] - g*h*np.sin(theta[k])
        theta[k+1] = theta[k] + h * v[k]/L
    return v, theta

h1 = T/N1
h2 = T/N2
v_pen1, theta_pen1 = pendel_euler(v0, theta0, g, L, N1, h1)
v_pen2, theta_pen2 = pendel_euler(v0, theta0, g, L, N2, h2)


plt.subplot(2, 1, 1)
plt.plot(t1,theta1, label='ϴ exact')
plt.plot(t1,theta_hat, label='ϴ estimate, N =2*5')
plt.plot(t1,theta_pen1, label = 'ϴ theta_pen, N = 2*5')
plt.legend()

plt.subplot(2, 1, 2)
N2 = 2**10
v_hat2, theta_hat2 = lin_pendel_euler(v0, theta0, g, L, N2, T)

theta = lin_pendel(t2, v0, theta0, g, L)

plt.plot(t2,theta2, label='ϴ exact')
plt.plot(t2,theta_hat2, label='ϴ estimate, N = 2**10')
plt.plot(t2,theta_pen2, label = 'ϴ theta_pen, N = 2*10')
plt.legend()
plt.show()
