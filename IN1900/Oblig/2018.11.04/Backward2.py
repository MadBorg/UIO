import numpy as np

class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)


class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h)-4*f(x-h)+3*f(x))/ 2*h



def f(t):
    return np.exp(-t)

def df(t):
    return -t* np.exp(-t)

t = 0
k = np.linspace(0,14,14+1)*-1
for i in k:
    B1 = Backward1(f)
    B2 = Backward2(f)
    yB1 = B1(t)
    yB2 = B2(t)
    dy = df(t)
    rel_err_B1 = abs(dy-yB1)/abs(dy)
    rel_err_B2 = abs(dy-yB2)/abs(dy)
    print(rel_err_B1, rel_err_B2)


'''
py.exe .\Backward2.py
.\Backward2.py:45: RuntimeWarning: divide by zero encountered in double_scalars
  rel_err_B1 = abs(dy-yB1)/abs(dy)
.\Backward2.py:46: RuntimeWarning: divide by zero encountered in double_scalars
  rel_err_B2 = abs(dy-yB2)/abs(dy)
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
inf inf
'''
