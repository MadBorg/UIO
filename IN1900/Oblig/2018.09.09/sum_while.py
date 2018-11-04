'''
s = 0; k = 1; M = 100
while k < M: #bolske utrykket utelukker k = m
s += 1/k # mangler indentering
#maa oke k for aa ungaa en uendelig lokke
print s # for py3 saa mangler paranteser


'''



s = 0; k = 1; M = 3
while k <= M:
    s+= 1/k
    k += 1
print(s)


'''
Terminal > sum_while.py
1.8333333333333333

Fikk samme svar med kalkulator
11/6 = 1.8333333333333333

'''
