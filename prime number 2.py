x = int(input("Enter the value = "))
for i in range(2,x):
    if x%i==0:
        print("It's not a prime number")
        break
else:
    print('It\'s a prime number')