from functools import reduce

lst = [1,44,6,22,56,23,55,34,8,879,9,3,32,45,76,94,35]

evens = list(filter(lambda a : a%2==0 , lst))
print('filtered list of even numbers = ',evens)

mapping = list(map(lambda a : a*2, evens))
print("\nDouble of each elements = ",mapping)

reducing = reduce(lambda a,b : a+b, mapping)
print("\nThe sum of the mapping elements = ",reducing)

list_tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list_tup.sort(key =lambda k:k[1])
print("\n",list_tup)

list_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
             {'make': 'Mi Max', 'model': '2','color': 'Gold'},
             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
list_dict.sort(key = lambda k:int(k['model']))
print("\n",list_dict)

