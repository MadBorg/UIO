
s = 0
M = 3

for k in range(1, M+1):  # retter fra 0 til M til 1 til M+1, bytter variabelen til k slik at vi den sammstemmer med funksjonen
    s += 1/2*k**2
print(s)


# alternativ while loop
s, k, M = 0, 1, M

while k <= M:  # stopper nor k er lik M
    s += 1/2*k**2
    k += 1  # oeker k slik at vi ikke far en uendelig loop
print(s)

'''
Terminal > sum_for.py
7.0
7.0
'''
