#2.1 Heaviside function
def heaviside(x):
    if x<0:
        return 0
    elif x >= 0:
        return 1

#2.2 Test function


def test_heaviside():

    x = [-1.0, 1.0]
    expected = [0.0, 1.0]
    tol = 1e-14
    calculated, boolV, msg = [],[],'|calculated - expected| > tol, i\n'
    for i in range(len(x)):
        calculated.append(heaviside(x[i]))
        boolV.append(abs(calculated[i] - expected[i]) < tol)
        if not boolV[i]:
            msg += '|{} - {}| = {} < {}, {}\n'.format(calculated[i], expected[i],abs(calculated[i] - expected[i]), tol, i)

    assert all(boolV), msg


test_heaviside()

#2.3 Numerical differentiation

def diff(f,x,h):
    df = (f(x+h)-f(x))/h
    return f(x), df

#2.3 Tabulated output
import numpy as np
def error_diff_sin():
    x = np.pi/4
    h = np.asarray([0.5**i for i in range(1,5)])
    f = np.sin

    analytical = -np.cos(x)
    numerical = diff(f,x,h)[1]
    err = abs(analytical - numerical)

    for i in range(len(h)):
        print('{:7.3f}{:7.3f}{:7.3f}'.format(x, h[i], err[i]))

#2.5 Prime numbers
def is_prime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True

num = list(range(2,10))
for i in num:
    print(i, is_prime(i))

#3.2 Forward Euler class

def solve(self, terminate=None):

    n = self.t.size
    u = self.u = np.zeros(n)
    self.u[0] = self.U0
    for k in range(n-1):
        self.k = k
        self.u[k+1] = self.advance()

    return self.u, self.t

def advance(self):
    u,f,k,t = self.u, self.f, self.k, slef.t
    dt = t[k+1] - t[k]
    u_new = u[k] + dt*f(u[k], t[k])
    return u_new

#3.3

class Heun(ForwardEuler):
    def advance(self):
        u,f,k,t = self.u, self.f, self.k, slef.t
        dt = t[k+1] - t[k]
        u_star = u[k] + dt*f(u[k], t[k])
        u_new = u[k] + dt/2 * f(u[k], t[k]) + dt/2 * f(u_star, t[k+1])
        return u_new


#3.4 Modeling with ODEs
def predator_prey(x0,y0,r,a,m,b,T,n):
    dx = lambda t: r*x-a*x*y
    dy = lambda t: -m*y + b*x*y
    solver = Heun
