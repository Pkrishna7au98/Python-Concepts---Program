
def squares():
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

nums = squares()

for i in nums:
    if i<=55:
        print(i)
    else:
        break

for i in nums:
    print(i)