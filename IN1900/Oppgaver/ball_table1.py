

def y(t, v0, g=9.8):
    y = v0*t-(1/2)*g*t**2
    return y

v0 = 10
n = 100
g = 9.8

interval = [0, 2*v0/g]
dt = abs(interval[0]-interval[1])/n
t = [interval[0] + dt * i for i in range(n+1)]

#a)
yt = []
for i in t:
    yi = y(i, v0)
    yt.append(yi)
    print('y({:.3f}) = {:.3f}'.format(i, yi))

#b)

print('\n---------------\n')
yt = []
i = interval[0]
eps = 1e-12
while i <= t[-1]+eps:
    yi = y(i, v0)
    yt.append(yi)
    print('y({:.3f}) = {:.3f}'.format(i, yi))
    i += dt

print(t[-1])
