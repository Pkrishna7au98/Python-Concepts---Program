from numpy import *

arr1 = array([ [1,2,3],[4,5,6] ])
arr2 = array([ [3,7,3],[1,5,6],[3,7,8]])

print(arr1)
print(arr2)


w = len(arr1)           # number of rows in array 1
x = len(arr1[0])        #number of coloumns in array 1
y = len(arr2)           # number of rows in array 2
z = len(arr2[0])        #number of coloumns in array 2

newarr = zeros(w*z,int)

j,m,r,n,p=0,0,0,0,0

while n<w:
    m=0
    j=0
    while m<z:
        l = 0
        k = 0
        while l<x:
            newarr[r] = newarr[r] + arr1[p,k] * arr2[k,j]
            k+=1
            l+=1
        m+=1
        j+=1
        r+=1
    n+=1
    p+=1

result = newarr.reshape(w,z)
print(result)


