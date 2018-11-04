def R(f,k,n, I=1, J=1):
    SUM = 0
    for i in range(I,n):
        for j in range(J, n):
            add = f(-k + (2*k*i)/n, -k + (2*k*j)/n)*((2*k)/n)**2
            SUM += add
            print("i =%g ,j = %g, n = %g, add = %g, sum = %g" %(i,j,n,add,SUM))
    return SUM



def f(x,y):
    return 1/(x**4 + 2*x**(2)*y + y**4 + 1)

r = R(f, 5, 5)
print(r)
