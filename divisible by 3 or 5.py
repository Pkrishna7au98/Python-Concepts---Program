h,i,j = 0,0,1
x = list(range(1,101))
while j<=100:
 if h<=99 or i<99:
   a = x[i] % 3
   b = x[h] % 5
   if (a==0 or b==0):
       print(x[i], end=" ")
   i += 1
   h += 1
   j += 1



