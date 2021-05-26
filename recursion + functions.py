

import sys

sys.setrecursionlimit(500)

print(sys.getrecursionlimit())
i=0
def welcome():
    global i
    i+=1
    print('hello', i)
    welcome()

welcome()