import ODESolver
import numpy as np
import matplotlib.pyplot as plt
dt = 0.5
nu = 0.1
days = 60 #for days >= 12 RuntimeWarning: overflow encountered in double_scalars; return [-beta1 *S*I, beta1*t*S*I - nu*I, nu*R]
n = int(days+1)
#beta = [float(1e-4*5),float(1e-4)]
beta1, beta2 = float(1e-4*5),float(1e-4)
t = np.linspace(0, days, n+1) #days
S = np.zeros(n+1)
I = np.zeros(n+1)
R = np.zeros(n+1)
S0, I0, R0 = 1500, 1, 0
S[0] = 1500; I[0] = 1; R[0] = 0

U0 = [S0, I0, R0]


'''
def ds(u, t):
    return -beta * S * I
def di(u,t):
    return beta* S * I - nu*I
def dr(u,t):
    return nu*I

def f(u,t):
    S,I,R = u
    return [-beta1 *S*I, beta1*S*I - nu*I, nu*I]
'''
class Logistic:
    def __init__(self, beta, nu, U0):
        self.beta, self.nu, self.U0 = beta, nu, U0

    def __call__(self, u, t):
        S, I, R = u
        return [-beta *S*I, beta*S*I - nu*I, nu*I]
c = 0 #counter
#for b in beta:
c += 1
f = Logistic(beta1, nu, U0)
solver = ODESolver.ForwardEuler(f)
solver.set_initial_condition(U0)
u, t = solver.solve(t)
#plt.subplots(len(beta),1,c)
plt.set_title("SIR, with b={}".format(beta1))
plt.plot(t,u)
plt.legend(['S', 'I', 'R'], loc = 'lower right')
plt.xlabel('days')

plt.show()
