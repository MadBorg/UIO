def primeTable(k):
    n= 5
    primelist = [2,3,5,7,11,17]
    print(primelist)

    diff = primelist
    for i in range(1,k):
        for j in range(n-i):
            print('diff[{}] = | (diff[{}]={}) - (diff[{}]={})| = {}'.format(
            j,j+1,diff[j+1],j,diff[j],  abs(diff[j+1] - diff[j])
            ))
            diff[j] = abs(diff[j+1] - diff[j])
        print('diff: ', diff)
        print(diff[:n-i])

primeTable(3)
