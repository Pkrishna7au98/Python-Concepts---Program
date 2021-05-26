class A:

    def __init__(self):
        print("Init for A")

    def feat1(self):
        print('Feature 1-A working')

class B(A):
    def __init__(self):
        super().__init__()
        print("Init for B")

    def feat2(self):
        print('Feature 2-B working')

class C(B):
    def __init__(self):
        super().__init__()
        print("Init for C")

    def feat(self):
        super().feat2()


b = C()
b.feat()