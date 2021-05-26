def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
x = int(input("Enter the value = "))
print("Factorial: {}".format(fact(x)))