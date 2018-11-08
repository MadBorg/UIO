import matplotlib.pyplot as plt
import numpy as np
#data = [[t1, v1],...,[ti, vi],...,[[tN],[vN]] #fart
t = list(range(0,10,2))
v = [2,4,8,12,24]
data = list(zip(t, v))
#print(data)
#a)
'''
Gi en algoritme for å beregne en tilnærming til objektets aksellerasjon
a(t) = v'(t) ut fra de beregnede verdiene (ti, vi) av farten
'''
def derivation(x,y):
    dy = [(y[i+1] - y[i])/ abs(x[i+1] - x[i]) for i in range(len(y)-1)]
    dy.append(0)
    return(dy)

#print(derivativeList(data))
#b)
'''
Gi en algoritme for å beregne en tilnærming til objektets avstand s(t) fra
startpunktet ut fra de beregnede verdiene når v(t) = s0(t) og s(t0) = 0.
'''
def integration(x,y):
    Y = [0]
    for i in range(1,len(y)):
        dx = x[i]-x[i-1]
        Y.append(y[i]*dx + Y[-1])
    return Y

#print(integration(data))

#c)


t = []
v = []
infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()
V = np.asarray(integration(t, v))
dv = np.asarray(derivation(t, v))

'''
plt.subplot(311)
plt.plot(t,v,label='v')
plt.legend()
'''


plt.subplot(211)
plt.plot(t,dv,label='derivative')
plt.legend()

plt.subplot(212)
plt.plot(t, V, label='integral')
plt.legend()

plt.show()
