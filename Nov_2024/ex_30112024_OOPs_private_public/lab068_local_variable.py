a= 10 #global variable

class person():
    b = 20 #instance variable

    def print_info(self):
        c = 30 #local variable
        print(c)
        print(self.b)
        global a
        print(a)



mannu = person()
mannu.print_info()