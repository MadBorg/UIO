
px = [0.8, 0.15, 0.45, 0.27, 0.05]

def E(px, x = None, start = 0):
    Ex = 0
    if x is None:
            x = range(start,len(px)+1)

    for i in range(0, len(px)):
        Ex += px[i]*x[i]
    return Ex

#print(E(px))
def V(px, x = None, start = 0):
    Ex = E(px)
    if x is None:
            x = range(start,len(px)+1)
    Vx = 0
    for i in range(0, len(px)):
        Vx = (x[i]-Ex)**2 * px[i]
    return Vx

print(V(px))

