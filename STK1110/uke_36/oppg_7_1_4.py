import numpy as np
x = [117,103,121,112,120,132,113,117,132,149,125,131,136,107,108,113,136,114]
y = [114,102,113,131,124,117,120,90,114,109,102,114,127,127,103]


averageX = sum(x)/len(x)
averageY = sum(y)/len(y)

print('averageX: {:.4f}, averageY {:.4f}'.format(averageX, averageY))

def SampleVariance(LIS):
    avg = sum(LIS)/len(LIS)
    q = 0
    for i in LIS:
        q += ((i - avg)**2)/(len(LIS)-1)
    return q

SampleVarianceX = SampleVariance(x)
SampleVarianceY = SampleVariance(y)
print('sqrt(SampleVarianceX): {:.4f}, sqrt(SampleVarianceY) {:.4f}'.format(np.sqrt(SampleVarianceX), np.sqrt(SampleVarianceY)))
