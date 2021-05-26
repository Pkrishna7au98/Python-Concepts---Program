class A:
    def f1(self):
        print('Feature 1 is working')
    def f2(self):
        print('Feature 2 is working')
class B(A):
    def f3(self):
        print('Feature 3 is working')


a= A()
b= B()

b.f1()
b.f2()
b.f3()
