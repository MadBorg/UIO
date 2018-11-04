sek = 10**9
min = sek/60
hour = min/60
days = hour/25
year = days/365
expected = 85

if year <= expected:
    print('the baby is expected to live longer than {:.1g} sek = {} years'.format(sek, year))
else:
    print(
        'the baby is not expected to live longer than {:.1g} sek = {} years'.format(sek, year))
