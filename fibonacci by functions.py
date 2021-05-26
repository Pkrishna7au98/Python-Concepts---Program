def fib(n):
    if n<=0:
        print("Sorry! Can't find the series")

    elif n==1:
        print(0)

    else:
        a,b= 0,1
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c

            if c>n:
                break
            else:
                print(c)

print("You'll get the fibonacci values less than the value you entered")

p = int(input('Enter Value = '))

fib(p)

