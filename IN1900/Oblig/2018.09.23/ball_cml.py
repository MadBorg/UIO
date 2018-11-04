import sys

v0, t = float(sys.argv[1]), float(sys.argv[2])
g = 9.81

y = v0*t - 0.5*g*t**2
print(y)

"""
Terminal > python .\ball_cml.py 1 1
-3.9050000000000002
"""
