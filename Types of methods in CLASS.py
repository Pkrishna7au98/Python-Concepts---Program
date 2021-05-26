class car:
    wheels = "Every car has four wheels"

    def __init__(self,brand,mileage,man_yr):
        self.m1 = brand
        self.m2 = mileage
        self.m3 = man_yr

    @classmethod               #CLASSMETHOD
    def get_wheels(cls):       #Argument must be 'cls' for classmethod
        print(cls.wheels)

    @staticmethod              #STATICMETHOD
    def static():              #Argument is not requied.
        print("Each car ia not electric vehicle")

c1 = car("BMW",15,2020)
c2 = car("Hyundai",18,2010)

print("Brand =",c1.m1,"Mil =",c1.m2,"Man_yr =",c1.m3)
car.get_wheels()     #classname.methodname()   #CLASSMEHTOD Output calling
car.static()         #classname.methodname()   #STATICMETHOD Output calling