class A:
    def execute(self):
        print("Compiler")
        print("Runing the code")

class B:
    def execute(self):
        print("Spell check")
        print("Compiler")
        print("Runing the code")

class C:
    def show(self,pp):
        pp.execute()

pp = B()

pp.execute()

er = C()
er.show(pp)


