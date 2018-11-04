from random import random
antfeil = 0
N = 100000
for i in range(N):
    x = random()
    y = random()
    z = random()

    res1 = (x*y)*z
    res2 = x*(y*z)
    if res1 != res2:
        antfeil += 1
        x0 = x
        y0 = y
        z0 = z
        ikkeass1 = res1
        ikkeass2 = res2
print(100. * antfeil/N, antfeil)
print(x0, y0, z0, ikkeass1 - ikkeass2)

'''
programmet tar 3 tilfelige flyttall fra 0 til 1.
Multiplisere verdiene i forskjellig rekkefølgeself.
    Først i res1 tar den produktet av x*y og multiplisere med z
    Så i res 2 tar programmet produktet av y*z og multiplisere det med  x
Det viser oss at selv om analytisk sett dette det samme, men siden dette
er numerisk så kappes desimaler av, og rundes av i under utregningenself.
dermed blir ikke ressultatet identisk.
Dette gjør programmet N-1 ganger, for å regne ut en feilprosentself.
Så printer programmet de siste to verdien som var feil.
'''
#b

from random import random
antfeil = 0
N = 100000
for i in range(N):
    x = random()
    y = random()
    z = random()

    res1 = x*(y+z)
    res2 = x*y+x*z
    if res1 != res2:
        antfeil += 1
        x0 = x
        y0 = y
        z0 = z
        ikkeass1 = res1
        ikkeass2 = res2
print(100. * antfeil/N, antfeil)
print(x0, y0, z0, ikkeass1 - ikkeass2)
