#Exception Handling in python
# Types of Exceptions : Compile Time :: Logical :: Run Time

a = 5
b = 2

try:
    print("Resourse Opened")
    print(a/b)
    k = int(input("Enter any number"))
    print(k)
except ZeroDivisionError as e:
    print("You can't divide a number by zero", e)
except Exception as e:
    print("Something went wrong")
finally:
    print("Resource Closed")