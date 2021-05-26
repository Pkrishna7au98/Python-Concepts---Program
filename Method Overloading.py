class A:
    def __init__(self):
        print('Sum of the given values is given below\n')

    def sum(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            s = a+b+c+d
        elif a!=None and b!=None and c!=None:
            s = a+b + c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

ram = A()
print(ram.sum(1,2,4))

