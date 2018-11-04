#ax2 + bx + c = 0
import numpy as np
def QuadSolutions(a,b,c):
    if (b**2 - 4*a*c) > 0:
        x1 = (b + sqrt(b**2 - 4*a*c))/ 2*a
        x2 = (b - sqrt(b**2 - 4*a*c))/ 2*a
        return x1, x2

    elif (b**2 - 4*a*c) < 0:

        x1 = (b + np.sqrt(complex(b**2 - 4*a*c)))/ 2*a
        x2 = (b - np.sqrt(complex(b**2+ - 4*a*c)))/ 2*a
        return x1, x2
    elif (b**2 - 4*a*c) == 0:
        x1 = x2 = (b + sqrt(b**2 - 4*a*c))/ 2*a
        return x1, x2
    else:
        print("something is wrong")

a,b,c = float(input('a: ')),float(input('b: ')),float(input('c: '))
print(QuadSolutions(a,b,c))

"""
PYTHON .\quadratic_roots_input.py
a: 1
b: 1
c: 1
((0.5+0.8660254037844386j), (0.5-0.8660254037844386j)
"""
