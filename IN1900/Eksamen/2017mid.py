import matplotlib.pyplot as plt
import numpy as np
import sys

def oppg1():
    year, mean_temp, min_temp, max_temp = [], [], [], []

    infile = open('data.txt')
    infile.readline()
    for line in infile:
        LineData = line.split()
        year.append(LineData[1]); mean_temp.append(LineData[2]); min_temp.append(LineData[3]); max_temp.append(LineData[4]);
    #print('{}\n\n{}\n\n{}\n\n{}'.format(year, mean_temp, min_temp, max_temp))

    plt.plot(year,mean_temp, label='mean_temp')
    plt.plot(year,min_temp, label='min_temp')
    plt.plot(year,max_temp, label='max_temp')
    plt.ylabel('Temperature'); plt.xlabel('Year')
    plt.legend()
    plt.show()
#oppg1()

def piecewise(x,a,b):
    if x <= a:
        return 0.0
    elif x > b:
        return 1.0
    elif a < x <= b:
        return (x-a)/(b-a)

#print(f(5,0,10))

def test_piecewise():
    a,b = 0, 1
    x= [-1.0,0.5,1.5]
    tol= 1e-14
    expected = [0.0,0.5,1.0]
    calculated = [piecewise(i,a,b) for i in x]
    err = [abs(i-j) for i,j in zip(expected, calculated)]
    boolL = [abs(i-j) < tol for i,j in zip(expected, calculated)]
    boolV = all(boolL)
    assert boolV, 'f({}) = {} != {}, error is {} '.format(x, calculated, expected, err)
#test_piecewise()
def oppg3c():
    try:
        x,a,b = float(sys.argv[1]),float(sys.argv[2]) ,float(sys.argv[3])
    except IndexError:
        print('innput 3 arguments in the Comand Line, must also be numbers')
    except ValueError:
        print('innput must be a number')
    piecewise(x,a,b)


def pi_approx(n):
    Sn = 0
    for k in range(1,n+1):
        Sn +=((-1)**(k+1))/(2*k-1)
    return Sn*4

    n = [10,100]
#print([pi_approx(i) for i in n])

def plot_pi_approx(f, start, stop):
    n  = np.arange(start, stop)
    y = [f(i) for i in n]
    plt.plot(n,y, label='plot_pi_approx')
    plt.ylabel('pi_approx'); plt.xlabel('n')
    plt.legend()
    #plt.show()

plot_pi_approx(pi_approx, 1, 50)
