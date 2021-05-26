from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(5):
            print(i)
            sleep(.5)

class B(Thread):
    def run(self):
        for i in range(5):
            print(5-i)
            sleep(.5)
r1 = A()
r2 = B()

r1.start()
r2.start()

r1.join()
r2.join()

print("Bye")