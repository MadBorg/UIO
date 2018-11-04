v1 = (0, 0)
v2 = (1, 0)
v3 = (0, 2)
vertices = [v1, v2, v3]


def triangle_area(vertices):
    x, y = [], []
    for i in vertices:  # converting vertices to the way described in the formula
        x.append(i[0])
        y.append(i[1])
    python = -1  # correcting for py counting from 0
    A = 1/2 * abs(x[2+python]*y[3+python] - x[3+python]*y[2+python] - x[1+python]
                  * y[3+python] + x[3+python]*y[2+python] - x[2+python]*y[1+python])
    return A


print(triangle_area(vertices))


def test_triangle_area():
    """ Verify the area of a triangle with vertex coordinates (0,0), (1,0), and (0,2). """
    v1 = (0, 0)
    v2 = (1, 0)
    v3 = (0, 2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol  # changed diff to abs
    msg = 'computed area=%g != %g (expected)' %\
        (computed, expected)
    assert success, msg


test_triangle_area()

'''
Terminal > area_triangle.py

1.0
'''
