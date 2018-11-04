import numpy as np
import matplotlib.pyplot as plt
x0,p,N = 100, 5, 4
index_set = range(N+1)
x = np.zeros(len(index_set))

#compute solution
x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (p/100) *x[n-1]
print(x)
plt.plot(index_set, x, 'ro')
plt.show()
