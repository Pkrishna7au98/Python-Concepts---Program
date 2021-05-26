
def rfn(x,y):
    p = 0
    z = range(x,y+1)
    for i in z:
        p = p+i
    return p
print(rfn(1,789))