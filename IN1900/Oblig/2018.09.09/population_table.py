def Nt(t, B, C, k, e=9.8):
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

interval = [0,48]
n = 10 #number of t values
dt = abs(interval[0]-interval[1])/n #step len
t = [interval[0]+dt*i for i in range(n+1)] #steps
N = [Nt(i, B, C, k) for i in t]#population per time


print(
'''
._______________________.
||    t     |    N     ||
||----------|----------||''')
for i, j in zip(t, N):
    print('|| - - - - -|- - - - - ||')
    print('||{:10.2f}|{:10.2f}||'.format(i, j))
print('''||----------|----------||
||    t     |    N     ||
._______________________.''')


'''
Terminal > population_table.py
._______________________.
||    t     |    N     ||
||----------|----------||
|| - - - - -|- - - - - ||
||      0.00|   5000.00||
|| - - - - -|- - - - - ||
||      4.80|  24923.28||
|| - - - - -|- - - - - ||
||      9.60|  44944.49||
|| - - - - -|- - - - - ||
||     14.40|  49379.05||
|| - - - - -|- - - - - ||
||     19.20|  49929.81||
|| - - - - -|- - - - - ||
||     24.00|  49992.14||
|| - - - - -|- - - - - ||
||     28.80|  49999.12||
|| - - - - -|- - - - - ||
||     33.60|  49999.90||
|| - - - - -|- - - - - ||
||     38.40|  49999.99||
|| - - - - -|- - - - - ||
||     43.20|  50000.00||
|| - - - - -|- - - - - ||
||     48.00|  50000.00||
||----------|----------||
||    t     |    N     ||
._______________________.
'''
