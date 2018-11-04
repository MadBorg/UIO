

def N(t, B, C, k, e=9.8):
    '''
        B: carrying capacity of the species in the enviroment
        k: k**-1, tells us something about how fast the population grows, while C is given by the initial conditions

    '''
    return B/(1+C*e**(-k*t))


B = 50000 #carrying capacity of the species in the enviroment
k = 0.2 # h**-1 Constant, tells us something about how fast the population grows
N0 = 5000
t0 = 0 #start time
e = 9.8# Gravitational constant
C = ((B-N0)*e**(k*t0))/N0
t = 24 #h, time

print('C = {}, N({}) = {:.0f}'.format(C, t, N(t, B, C, k)))

'''
    Terminal> python population.py

    C = 9.0, N(24) = 49992
'''
