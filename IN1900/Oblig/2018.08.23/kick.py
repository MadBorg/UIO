from numpy import pi
CD = 0.4  # Drag coeffivient
q = 1.2  # kg density of the air
a = 0.11  # m, radius
A = pi*a**2  # crossectional area
kmh2ms = 5/18
V = [120*kmh2ms, 30*kmh2ms]   # km/h Velocity of the object
g = 9.81  # m *s**-2
m = 0.43  # kg mass
Fg = m*g  # Gracity force on an object
print('Fg = {:.1f} N '.format(Fg))
comments = ['Fast', "Slow"]


def Fd(CD, q, A, V):
    return (1/2*CD*q*A*V**2)


for i in range(len(V)):
    F_d = Fd(CD, q, A, V[i])
    ratio = F_d / Fg
    print('{} kick \nF_{:.2f} = {:.2f} N,\nratio of the drag force and the gravity force:\nF_{:.2f}/Fg = {:.2f}\n'.format(
        comments[i], V[i], F_d, V[i], ratio))


'''
        Fg = 4.2 N
    Fast kick
    F_33.33 = 10.14 N,
    ratio of the drag force and the gravity force:
    F_33.33/Fg = 2.40

    Slow kick
    F_8.33 = 0.63 N,
    ratio of the drag force and the gravity force:
    F_8.33/Fg = 0.15

'''
