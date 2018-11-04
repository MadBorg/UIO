
def INFILE():
    infile = open(
        'C:/Users/redna/OneDrive - Universitetet i Oslo/UIO/IN1900/Forelesning/2018.09.13/data.txt', 'r')
    lines = infile.readlines()
    for s in lines:
        print(s)
    infile.close()


# INFILE()

file_path = 'C:/Users/redna/OneDrive - Universitetet i Oslo/UIO/IN1900/Forelesning/2018.09.13/rome.txt'
rw = 'r'


def read_rain_rome(file_path, rw, Print=False):
    infile = open(file_path, rw)
    col1, col2 = [], []
    for line in infile:
        words = line.split()
        col1.append(words[0])
        col2.append(float(words[1]))
    infile.close()
    name_month = col1[:-1]
    rain_month = col2[:-1]
    rain_year = col2[-1]
    return [name_month, rain_month, rain_year]
    if Print == True:
        for i, j in zip(name_month, rain_month):
            print(i, j)
    else:
        pass


name_month, rain_month, rain_year = read_rain_rome(file_path, rw)


expr = 'x + 3*x - 5*x**2'
x = 0.5


def f(x, Print=False):
    res = eval(expr)
    return res
    if Print is True:
        print('f({}) = {}'.format(x, res))
#f(x, True)


def sysex():
    import sys
    from math import *
    expr = sys.argv[1]
    xval = [float(1)/1000 for i in range(0, 1001)]
    yval = [eval(expr) for x in xval]
    print('Maximal value on [0,1]: %5.2f' % max(yval))
