import ODESolver
import SIR_class
import numpy as np
import matplotlib.pyplot as plt


class ProblemSIRV(ProblemSIR):
    def __init__(self, beta, nu, p, U0, T):
        ProblemSIR.__init__(self, beta, nu, U0, T)
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

    def __call__(self, u, t):
        beta, nu, p, U0 = self.beta, self.nu,self.p, self.U0
        S, I, R, V = u
        return [-beta(t)*S*I - p(t)*S, beta(t)*S*I - nu(t)*I, nu(t)*I, p(t)*S]

    
