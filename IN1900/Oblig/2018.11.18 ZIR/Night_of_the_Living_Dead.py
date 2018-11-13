from SIR_class import *



def coefs(t):
    if 0<= t <=4: #initial phas
        alfa = 0
        beta = 0.03
        delta_I = 0
        delta_S = 0
        SIGMA = 20
        rho = 1
        return [alfa, beta, delta_S, delta_I, rho, SIGMA]
    elif 4< t <=28: #hysterical phase
        alfa = 0.0016
        beta = 0.0012
        delta_I = 0.014
        delta_S = 0
        SIGMA = 2
        rho = 1
        return [alfa, beta, delta_S, delta_I, rho, SIGMA]
    elif 28< t <= 33: #Counter attack
        alfa = 0.006
        beta = 0
        delta_I = 0
        delta_S = 0.0067
        SIGMA = 0
        rho = 1
        return [alfa, beta, delta_S, delta_I, rho, SIGMA]


alfa = lambda t: 
