i=0
ac = 4
x = int(input("Enter the candies you need = "))
for i in range(x):
    if i>=ac:
        print("Out of Stock")
        break
    if i<=x:
        print("candy")
    i+=1