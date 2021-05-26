f=1
def search(self,n):
    global f
    for i in list:
        if i==n:
            return True,f
        f+=1
    else:
        return False

list = [1,3,7,8,5,9]

if search(list,9):
    print("Found at", f)
else:
    print("Not found")

