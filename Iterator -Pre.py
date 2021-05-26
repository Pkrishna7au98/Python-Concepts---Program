nums = [2,6,3,7,3,2,1]

it = iter(nums)

print(it.__next__())
print(next(it))

for i in nums:
    print(i)