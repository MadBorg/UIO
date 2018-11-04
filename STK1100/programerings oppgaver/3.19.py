import numpy as np
def prob(x):
    return np.log10((x+1)/x)

Sum = 0
probs = {}
for i in range(1,10):
    proba = prob(i)
    Sum += proba
    probs[i] = proba

print(Sum, "\n", probs)