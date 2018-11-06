def integration(x,y):
    Y = [0]
    for i in range(1,len(y)):
        dx = x[i]-x[i-1] 
        Y.append(y[i]*dx + Y[-1])
    return Y




x = [0,1,2,3,4]
y = [0,1,2,3,4]

print(integration(x,y))
