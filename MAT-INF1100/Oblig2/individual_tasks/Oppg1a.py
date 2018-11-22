import matplotlib.pyplot as plt
import numpy as np

#a)
'''
Gi en algoritme for å beregne en tilnærming til objektets aksellerasjon
a(t) = v'(t) ut fra de beregnede verdiene (ti, vi) av farten
'''
def aksellerasjon(x,y):
    dy = [(y[i+1] - y[i])/ abs(x[i+1] - x[i]) for i in range(len(y)-1)]
    return(dy)


if __name__ == "__main__":
    t = list(range(0,10,2))
    v = [2,4,8,12,24]

    print(t[1:],aksellerasjon(t,v))
