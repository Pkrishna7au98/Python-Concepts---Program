print("Operation code = 0 (Addition) , 1 (Multiplication)")
x = int(input('Enter code = '))

p = int(input('Enter first value = '))
q = int(input('Enter second value = '))

if x==0:
    f = lambda a,b : a+b
    result = f(p,q)
    print(result)
else:
    f = lambda a, b: a * b
    result = f(p, q)
    print(result)
