def sum(a,b):
    def sum1():
        c=a+b
        return c
    return sum1()+5

a = int(input('Enter first value = '))
b = int(input('Enter second value = '))
result = sum(a,b)
print(result)