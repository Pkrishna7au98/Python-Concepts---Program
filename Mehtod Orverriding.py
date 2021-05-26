class father:
    def show(self):
        print("Father is young")

class child(father):
    def show(self):
        print("I am younger")


a = child()

a.show()


