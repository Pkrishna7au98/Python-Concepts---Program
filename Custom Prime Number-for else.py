x = int(input("Enter the value = "))
rg = range(2, x)
if x==2:
    print("You're not joking, Right?")

for i in rg:
    if x % i != 0:
        continue
    else:
        print(" It's not a prime number")
        break
else:
    if x==1:
        print("Not prime my dear friend")
    else:
        print("It's a prime number")