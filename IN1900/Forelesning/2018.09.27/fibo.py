import numpy as np

n = 100
x = np.zeros(n+1, int)
x[0], x[1] = 1,1
for i in range(2,n):
    x[i] = x[i-1] + x[i-2]

print(x)
