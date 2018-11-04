
#a
def binom3(n, i):
    prod = 1
    for j in range(1, n-i+1):
        prod *= (i+j)/j
    return prod
print(binom3(5,3))


def test_binom3():
    test_input = [[int(5e3), 4], [int(1e5), 60], [int(1e3), 500]]
    calculated = [binom3(i[0], i[1]) for i in test_input]
    expected = [26010428123750, 1.18069197996257e218, 2.702882409454366e299]
    rellative_error = [abs(j-i) / abs(j) for i, j in zip(calculated, expected)]

    return calculated, rellative_error
print(test_binom3())
'''
for å forklare at vi må bruke flyttall, vil jeg bruke eksempelet. binom3(5,3)
som med den siste j'en i loopen. gir brøken (5+3)/3 som er 2**3/3 som ikke er
delelig med 3. dermed får vi flyttall.
'''
#d
'''
Med mindre binomialen er over owerflow. Får vi ikke owerflow siden i+j er alltid mindre enn det nåverdende produktet
'''
#c
def binomC(n, i):
    prod = 1
    for j in range(1, n-i+1):
        prod *= (n-j)/j
    return prod

binomC(5,3)


def test_binomC():
    test_input = [[int(5e3), 4], [int(1e5), 60], [int(1e3), 500]]
    calculated = [binomC(i[0], i[1]) for i in test_input]
    expected = [26010428123750, 1.18069197996257e218, 2.702882409454366e299]
    rellative_error = [abs(j-i) / abs(j) for i, j in zip(calculated, expected)]

    return calculated, rellative_error
print(test_binom3())
