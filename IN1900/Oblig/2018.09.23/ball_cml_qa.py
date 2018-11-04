
try:
    import sys
    v0, t = float(sys.argv[1]), float(sys.argv[2])
except IndexError:
    v0, t = float(input('v0: ')), float(input('t: '))

g = 9.81

y = v0*t - 0.5*g*t**2
print(y)

"""
Terminal > python .\ball_cml_qa.py
v0: 1
t: 1
-3.9050000000000002

Terminal > python .\ball_cml_qa.py 1 1
-3.9050000000000002

"""
