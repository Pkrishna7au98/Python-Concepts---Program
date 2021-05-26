class computer:      #OUTER CLASS
    def __init__(self,name,storage):       # OUTER CLASS CONSTRUCTOR
        self.n = name
        self.a = storage
        self.warr = self.warranty()        #ASSIGNING WARRANTY CLASS AS A VARIABLE IN COMPUTER CLASS

    def show(self):                        #OUTER CLASS SHOW FUNCTION TO FETCH DETAILS
        print(self.n , self.a)
        self.warr.show()           #FETCHING SHOW FUNCTION DETAILS OF CLASS WARRANTY IN CLASS COMPUTER


    class warranty:                        #INNER CLASS
        def __init__(self):                #INNER CLASS CONSTRUCTOR
            self.start = 2013
            self.end = 2025
            self.drn = self.end - self.start

        def show(self):                    #INNER CLASS SHOW FUNCTION TO FETCH WARRANTY CLASS DETAILS
            print(self.start,self.end,self.drn)

com1 = computer('I5 PC',1024)
com2 = computer('Ryzen PC', 2048)

com1.show()      # THIS MEANS : SHOW FUNCTION IS CALLED FOR COM1 AND COM2 OBJECTS
com2.show()      # SHOW FUNCTION INCLUDES THE DETAILS OF ANOTHER SHOW FUNCTION OF CLASS WARRANTY






