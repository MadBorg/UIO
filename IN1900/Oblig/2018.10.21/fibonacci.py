import numpy as np
N = 15
x = np.zeros(N)
x[0], x[1] = 1,1
for n in range(2,N):
    x[n] = x[n-1] + x[n-2]

print(x)


'''

python fibonacci.py

[  1.   1.   2.   3.   5.   8.  13.  21.  34.  55.  89. 144. 233. 377.
 610.]

'''
