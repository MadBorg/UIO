

def f2c(f):
    #Founction for converting
    #F = (9/5)*c+32
    C = (f-32)*5/9
    return C

def f2c_approx(f):
    #Function for approxing the converson if f to c
    C = (f-30)/2
    return C

print('''
.__________________________.
|   F    |   C    |   Ĉ    |
|--------|--------|--------|''') #making a nice hedding
for f in range(0,100, 10): #running through a list from 0 to 100, with a steplenght of 10
    C = f2c(f) #calculating C
    C_approx = f2c_approx(f) #calculating an approximation for C
    print('|{:8.3f}|{:8.3f}|{:8.3f}|'.format(f, C, C_approx))#creating a nice print

'''
Terminal > f2c_approx_table.py

.__________________________.
|   F    |   C    |   Ĉ    |
|--------|--------|--------|
|   0.000| -17.778| -15.000|
|  10.000| -12.222| -10.000|
|  20.000|  -6.667|  -5.000|
|  30.000|  -1.111|   0.000|
|  40.000|   4.444|   5.000|
|  50.000|  10.000|  10.000|
|  60.000|  15.556|  15.000|
|  70.000|  21.111|  20.000|
|  80.000|  26.667|  25.000|
|  90.000|  32.222|  30.000|


'''
