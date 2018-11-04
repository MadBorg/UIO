# 2.1 Make a Fahrenheit-Celsius converson table




F = 0
dF = 10


while F <= 100:
    C = f2c(F)
    F += dF
    print('{:.2f}F = {:.2f}C'.format(F, C))
