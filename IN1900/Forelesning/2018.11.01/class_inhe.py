class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
    def __call__(self, x):
        return self.c0+self.c1*x
    def table(self,L,R,n):
        '''Return a Table with n points for L <= x <= R.'''
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n'
        print(s)


class Parabola0(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self,c0,c1)
        self.c2 = c2
    def __call__(self, X):
        return self.c0 + self.c1*x + self.c2*x**2
        #return Line(x) + self.c2*x**2
