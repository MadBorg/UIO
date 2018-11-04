def y(t, v0, g=9.81):
    return v0*t - 1/2*g*t**2


n = 10
v0 = 5
g = 9.81
t_stopp = 2*v0/g
dt = t_stopp/n

for i in range(n+1):
    t = i * dt
    yt = y(t, v0, g)
    print('y({:5.2f}) = {:5.2f}'.format(t, yt))

Ɛ = 1e-10

t = 0
while t < t_stopp + Ɛ:
    yt = y(t, v0, g)
    print('y({:5.2f}) = {:5.2f}'.format(t, yt))
    t += dt
