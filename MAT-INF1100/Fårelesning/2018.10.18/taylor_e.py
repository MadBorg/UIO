import math as m

n = 20
add = 1
ee = 2

for k in range(2,n+1):
    add = add/k
    ee = ee + add

print(f'n = {k:2}, ee = {ee:16.f}, k = {m.e-ee:.2g}')
