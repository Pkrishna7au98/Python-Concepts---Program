x = int(input("Enter the number = "))
a= list(range(2,x))
if x==2:
    print("It's the first prime number")
else:
    for i in a:
        if x%a[i]!=0:
            print("It's prime number")
        else:
            print("It's not a prime number")




