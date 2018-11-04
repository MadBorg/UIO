p = 5 # percent interest rate
n = 3 #years
A = 1000 # initial amount
EndAmount = A*((1 + p/100)**n)
print('EndAmount = {:.1f}'.format(EndAmount))

"""
Terminal> python interest_rate.py

EndAmount = 1157.6 aur

"""
