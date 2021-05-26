class A:
    def f1(self):
        print('Feature a1 is working')

    def f2(self):
        print('Feature a2 is working')


class B(A):
    def f3(self):
        print('Feature b3 is working')


class C(B):
    def f4(self):
        print('Feature c4 is working')

    def f5(self):
        print('Feature c5 is working')

    def f6(self):
        print('Feature c6 is working')


a = A()
b = B()
c = C()

a.f1()
a.f2()

b.f1()
b.f2()
b.f3()

c.f1()
c.f2()
c.f3()
c.f4()
c.f5()
c.f6()

