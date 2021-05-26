from numpy import *

arr1 =([7657,23,20])
arr2 =([44,55,45,34,23])

newarr = zeros(len(arr1)+len(arr2),int)
print(newarr)

p=0
q= len(arr1)
for i in arr1:
    newarr[p]= i
    p+=1
for i in arr2:
    newarr[q] = i
    q+=1


print(newarr)
