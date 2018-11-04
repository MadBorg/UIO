import numpy as np
def f(x):
    return np.log(x)
interval= np.linspace(1,10,101)
x = np.zeros(len(interval))
y = np.zeros(len(interval))
for i in range(len(interval)):
    y[i] = f(interval[i])
    x[i] = interval[i]

#for i,j in zip(x,y):
#    print(i,j)
