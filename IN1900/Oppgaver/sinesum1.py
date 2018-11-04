import numpy as np

def f(t, T):
    if 0<t<T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2<t<T:
        return -1

def S(t, n, T):
    x = 0
    for i in range(n+1):
        x += (1/(2*i-1))*np.sin((2*(2*i-1)*np.pi*t)/T)
    return x*4/np.pi


def f_S_ErrorTable(f,S):
    n = np.array([1,3,5,10,30,100])
    a =np.array([0.01,0.25,0.49])
    T = 2*np.pi
    t = a*T
    data = {'f':None,'S':None,'Error':None}
    fv,Sv = np.vectorize(f), np.vectorize(S)
    Stn = np.array([Sv(t, i, T) for i in np.nditer(n)])
    ft = fv(t,T)
    err = Stn - ft
    #relerr =
    return Stn, err




Stn, err = f_S_ErrorTable(f,S)
print('{}\n\n{}'.format(Stn, err))

#print(f_S_ErrorTable(f,S))
