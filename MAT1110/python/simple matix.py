import numpy as np
import matplotlib.pyplot as plt


theta = np.pi/2
x = 1
T11, T12, T21, T22 = x*np.cos(theta), x*(np.sin(theta)), x*np.sin(theta), x*-(np.cos(theta))
A1, A2 = 1, 1
TA1, TA2 = T11*A1+T12*A2, T21*A1+T22*A2
print(A1, A2)
print(TA1, TA2)
plt.plot(A1, A2 , "ro")
plt.plot(TA1, TA2, "ro")
plt.axis([-5,5,-5,5])
plt.show()



"""
class vectormanipulation:
    def __init__(self):

    def mirror_x(self):
"""