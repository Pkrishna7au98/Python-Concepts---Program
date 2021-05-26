class Student:
    def __init__(self,m1,m2,m3):
        self.maths = m1
        self.eng = m2
        self.hindi = m3
        sum = m1+m2+m3

    def __add__(self,other):
        m1 = self.maths + other.maths
        m2 = self.eng + other.eng
        m3 = self.hindi + other.hindi
        s4 = Student(m1, m2, m3)
        return s4

    def sum(self):
        sum = self.maths + self.eng + self.hindi
        return sum

s1 = Student(22,53,23)
s2 = Student(23,46,68)
s3 = Student(25,36,23)
s4= s1+s2+s3

print("sum of marks of s1 = {}".format(s1.sum()))
print("sum of marks of s2 = {}".format(s2.sum()))
print("sum of marks of s3 = {}\n".format(s3.sum()))
print("Sum of marks in maths = {}".format(s4.maths))
print("Sum of marks in english = {}".format(s4.eng))
print("Sum of marks in hindi = {}".format(s4.hindi))