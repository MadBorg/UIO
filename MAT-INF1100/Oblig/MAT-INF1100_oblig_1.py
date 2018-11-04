import numpy as np
import math as m

x0, x1, n = 1, 2,  100

#a
def DiffEq(x0, x1, n):
    x = [x0, x1]
    for i in range(n-1):
        x.append(2*x[i+1] + x[i])
    return x

# b)
x1 = 1-m.sqrt(2)
x_list = DiffEq(x0, x1, n)
counter = 0
for i in x_list:
    print('x({}) = {}'.format(counter, i))
    counter += 1

# print(x)

# c


def GeneralEq(n):
    return (1-m.sqrt(2))**n


# d
x_simu = DiffEq(x0, x1, n)
x_general = [GeneralEq(i) for i in range(len(x_simu))]
counter = 0
relative_error = []
for i, j in zip(x_simu, x_general):
    relative_error.append(abs(i-j)/abs(j))
    print('n: {:5.1f} ,x_simu: {:12.6g}, x_general: {:12.6g}, rel_err: {:12.6g}'.format(
        counter, i, j, relative_error[counter]))
    counter += 1

y = relative_error
x = [i for i in range(len(y))]

import matplotlib.pyplot as plt
plt.plot(x, y)
axes = plt.gca()
axes.set_xlim([0, len(x)])
axes.set_ylim([-1, 1.2e+60])
plt.show()

'''
Vi har store avvik i den simulerte løsningen pga summeringen av et heltall og roten av 2.
hver gang vi legger sammen kuttes noen desimaler. Og som vist i rel_err så blir feilen fort storself.
'''
