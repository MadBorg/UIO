import numpy as np


def f(x):
    if x > 0:  # hvis x er stoerre enn 0 soe returneres sin(x)
        return np.sin(x)
    elif x <= 0:  # hvis x er mindre eller lik 0 saa returneres 0
        return 0
    else:  # hvis dette blir kjoert har det skjedd noe feil
        print("WRONG!!!!")
        quit()


def test_f():
    """ """
    x = np.pi/4  # test x'en
    expected = 1/np.sqrt(2)  # den forventede verdien regnet ut i externt program
    computed = f(x)  # regner ut f(x) med min funksjon
    tol = 1E-14  # toleransen
    success = abs(expected - computed) < tol
    msg = 'f({}) != {} (expected)'.format(
        x, computed)  # printer hvis assert feiler
    assert success, msg
