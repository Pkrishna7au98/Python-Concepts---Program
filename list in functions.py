print('Hi There! : Enter the names')

names = []

k=0
while k<10:
    z = input("Name:{} = ".format(k+1))
    names.append(z)
    k+=1

def count():
    upto5 = 0
    above5 = 0
    for i in names:
        if len(i)<=5:
            upto5+=1
        else:
            above5+=1
    return upto5,above5

upto5 , above5 = count()

print("upto5 : {} and above5 : {}".format(upto5,above5))