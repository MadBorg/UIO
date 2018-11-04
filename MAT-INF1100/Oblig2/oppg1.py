import matplotlib.pyplot as plt
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
def derivation(list):
    derivative = [[list[i][0], \
     (list[i+1][1] - list[i][1])/ abs(list[i+1][0] - list[i][0])] \
     for i in range(len(list)-1)]
    return(derivative)

#print(derivativeList(data))
#b)
'''
Gi en algoritme for å beregne en tilnærming til objektets avstand s(t) fra
startpunktet ut fra de beregnede verdiene når v(t) = s0(t) og s(t0) = 0.
'''
def integration(list):
    integral = [[0,0]]
    for i in range(len(list)-1):
        integral.append([list[i+1][0],\
         ((list[i+1][1] - list[i][1])*abs(list[i+1][0] - list[i][0])) +sum(i for i, _ in integral)] )
    return(integral)

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
data = [[i,j] for i,j in zip(t,v)]
integral = integration(data)
derivative = derivation(data)


plt.subplot(311)
plt.plot(t,v,label='v')
plt.legend()
plt.subplot(312)
t, dv = zip(*derivative)
plt.plot(t,dv ,label='derivative')
plt.legend()
plt.subplot(313)
t, V = zip(*integral)
plt.plot(t, V, label='integral')
plt.legend()
plt.show()
