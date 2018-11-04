class Line(object):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def line(self):
        y0, y1 = self.p1
        x0, x1 = self.p2
        a = (y1 - y0)/(x1 - x0)
        b = y0 - a*x0
        return a, b

    def value(self, x):
        a, b = self.line()
        return a*x + b


def test_Line():
    p1 = (0,-1)
    p2 = (2,4)
    L = Line(p1, p2)
    valu = [L.value(i) for i in (0.5, 0, 1)]
    exact = (0.25, -1.0, 1.5)
    tol = 1e-14
    err = [abs(i - j) for i,j in zip(valu, exact)]
    max_err = max(err)
    assert max_err >= tol, 'err <= tol'

test_Line()

'''
py.exe .\Line.py
#ingen print siden testen ikke feiler
'''
