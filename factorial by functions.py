x = int(input("Enter the value for factorial = "))

def fact(p):
    k=1
    for i in range(1,p+1):
        k = k*i
    return k

fact(x)
print("Factorial = ",fact(x))