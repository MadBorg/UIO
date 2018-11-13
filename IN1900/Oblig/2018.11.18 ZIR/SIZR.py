from SIR_class import *


class ProblemSIZR(ProblemSIR):
    """docstring for SIZR."""
    def __init__(self, coefs, U0, T, tol=1e-10):

        self.coefs = [] # alfa, beta, delta_S, delta_I, rho, SIGMA
        for i in range(len(coefs)):
            if isinstance(coefs[i], (float, int)):
                self.coefs.append(lambda t: coefs[i])
            elif callable(ceofs[i]):
                self.coefs.append(coefs[i])

        self.U0, self.T = U0, T


    def __call__(self, u, t):
        S,I,Z,R = u
        alfa, beta, delta_S, delta_I, rho, SIGMA = self.coefs
        dS = SIGMA(t) - beta(t)*S*Z-delta_S(t)*S
        dI = beta(t)*S*Z - rho(t)*I - delta_I(t)*I
        dZ = rho(t)*I - alfa(t)*S*Z
        dR = delta_S(t)*S + delta_I(t)*I + alfa(t)*S*Z
        return [dS, dI, dZ, dR]

# alfa, beta, delta_S, delta_I, rho, SIGMA
alfa = 0.0016
beta = 0.0012
delta_I = 0.014
delta_S = 0
SIGMA = 2
rho = 1
S0 = 10
Z0 = 100
I0 = 0
R0 = 0
T = 24 #hours
dt = 0.01
U0 = [S0, I0, Z0, R0]
coefs = [alfa, beta, delta_S, delta_I, rho, SIGMA]

if __name__ == "__main__":
    problem = ProblemSIZR(coefs, U0, T)
    solver = SolverSIR(problem, dt)
    solver.solve(terminate=problem.terminate)
    solver.plot(labels=['S', 'I', 'Z', 'R'], title='SIZR')
    plt.show()
