# Defining the class named as COMPUTER
class computer:

    # Defining method 1
    def __init__(self):
        print('Hello')

    # Defining method 2
    def configuration(self):
        print("I5, 16 GB , 4TB ")

 # Telling the interpreter that com1,com2 variables belong to class COMPUTER
com1 = computer()
com2 = computer()

# From class COMPUTER , Method 2 is applied to viriables Com1,Com2
computer.configuration(com1)
computer.configuration(com2)






