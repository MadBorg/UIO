def avstand(x,y):
    Y = [0]
    for i in range(1,len(y)):
        dx = x[i]-x[i-1]
        Y.append(y[i]*dx + Y[-1])
    return Y

if __name__ == "__main__":
    t = list(range(0,10,2))
    v = [2,4,8,12,24]

    print(t, avstand(t,v))
