import numpy as np
#definerer funksjonen R(n,k), funksjonens parametere er en funksjon av to variable, interger n som bestemmer antall iterasjoner, og k som er et ledd i funksjonen
def R(f, n, k):
    # s er summen som er vår retun verdi
    s = 0
    #implementerer begge summene, 1. fra 1 til n, 2. fra 1 til n
    for i in range(1,n):
        for j in range(1,n):
            # regner først ut f og lager den som "func"
            func = f(-k+(2*k*i)/n, -k+(2*k*j)/n)
            #legger func sammen med resten av funksjonen
            l = func*((2*k)/n)**2
            #leggerr leddet til i summen
            s += l
            #print ('s = %.5d, f = %.4f, j = %g, i = %g, l = %g' % (s, func, j, i, l)) # # debug hjelp

    return s
#funksjonen f som legges til som et parameter i R, avhengig av to variable
def f(x,y):
    return 1/(x**4 + 2*x**2*y**2 + y**4 + 1)

#parameter verdiene
n, k = 1000, 177
#den eksate verdien vi er ute etter
val = ((np.pi)**2)/2

#print ('n = %g, k = %g')
#kjører funksjonen og lagrer verdien til Res
Res = R(f, n, k)
#printer ressultater, R = Res printer resultatet, |R-val| = abs(Res - val) printer feilen på tilnermingen R, val = val er verdien vi er ute etter
print('R = %g, |R - val| = %g, val = %g '  % (Res, abs(Res - val), val) )

"""
kjøreeksempel
PS C:\Users\SKJSA> python ".../oppg1.py"
R = 4.93473, |R - val| = 7.27199e-05, val = 4.9348
"""
