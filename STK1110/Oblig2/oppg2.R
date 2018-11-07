AN = 31
BN = 31
AMean = 93.32
BMean = 96.58
AStDev = 15.41
BStDev = 13.84
ASE_Mean = 2.77
BSE_Mean = 2.49

DN = 31
DMean = -3.26
DStDev = 8.81
DSE_Mean = 1.58

alfa = 0.05

t_CI = DMean + c(1,-1)*qt(alfa/2, DN-1)*DStDev/sqrt(DN)
