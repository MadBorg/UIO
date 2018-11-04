import numpy as np
import matplotlib.pyplot as plt
x0,p,N = 100, 5, 4

#compute solution
outfile = open('growth_years_efficient_data.dat', 'w+')
xp, n = x0, 0
while n <= N:
    x = xp + (p/100) *xp
    outfile.write('{} {:10.4f}\n'.format(n, x))
    xp = x; n += 1
outfile.close()

'''
python growth_years_efficient.py

#lager en fil med navn growth_years_efficient_data.dat og innhold:
0   105.0000
1   110.2500
2   115.7625
3   121.5506
4   127.6282

'''
