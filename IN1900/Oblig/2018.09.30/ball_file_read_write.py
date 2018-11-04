
# a


def ReadInitData(file):
    infile = open(file)
    line1 = infile.readline().split()  # print(line1)
    v0 = float(line1[1])
    infile.readline();  # skip line
    t_raw = infile.read().split()
    # print(t_raw)
    t = [float(i) for i in t_raw]
    # print(t)
    infile.close()
    return v0, t


file = 'ball.dat'
v0, t = ReadInitData(file)
#print(v0, t)

# b


def test_ReadInitData():

    expected_V0 = 4
    expected_x = [i for i in range(0, 10)]

    file = "test_ReadInitData.dat"
    outfile = open(file, "w+")
    outfile.write('v0: {} \nt: \n'.format(expected_V0))
    for i in expected_x:
        outfile.write('{}\n'.format(i))
    outfile.close()
    computed_v0, computed_x = ReadInitData(file)
    t_bool, v0_bool = computed_x == expected_x, computed_v0 == expected_V0
    assert (t_bool and v0_bool), "test_x == x = {}, test_v0 == v0 = {}".format(t_bool, v0_bool)
    import os
    os.remove(file)


test_ReadInitData()

# c)


def y(t, v0, g=9.81):
    return v0*t-0.5*g*t**2


def write_res(y, infileName, outfileName='res.dat'):
    outfile = open(outfileName, "w+")
    v0, t = ReadInitData(infileName)
    t.sort()
    y_vals = [y(i, v0) for i in t]
    outfile.write('|    t    |    y    |\n')
    for i, j in zip(t, y_vals):
        outfile.write('|{:9.5f}|{:9.5f}|\n'.format(i, j))
    return t, y_vals, v0


write_res(y, 'ball.dat')
