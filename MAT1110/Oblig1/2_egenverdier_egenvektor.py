def eig(A):
    import  numpy as np
    a11,a12,a21,a22 = A
    a = 1
    b = -a22*-a11
    c = a11*a22- a12*a21
    print("a= ", a,"b = ",b,"c = ",c)
    x1 = (-b + np.sqrt((-b)**2 - 4*a*c)) / 2*a
    x2 = (-b - np.sqrt((-b)**2 - 4*a*c)) / 2*a
    λ = (x1, x2)

    a,b,c,d = a11, a12, a21, a22
    x = 1
    y1 = ((λ[0]-a))/b

    y2 = ((λ[1]-c))/d


    return (" λ = %g, %g;\n y1 = %g;\n y2 = %g\n" % (x1,x2, y1, y2))


A = [2,1,1,2]
print(eig(A))




