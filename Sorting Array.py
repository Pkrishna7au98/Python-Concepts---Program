from array import *

arr = array('i', [1,4,8,3,8,44,24,67])
i=0
while i<8:
    print(min(arr), end=" ")
    arr.remove(min(arr))
    i+=1



