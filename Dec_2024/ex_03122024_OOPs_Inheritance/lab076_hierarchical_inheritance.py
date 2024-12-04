class Father():
    def BHK1(self):
        print("1BHK")

class Amar(Father):
    def BHK2(self):
        print("2BHK")

class Akbar(Father):
    def BHK3(self):
        print("3BHK")

class Anthony(Father):
    def BHK(self):
        print("No House")


obj_1 = Amar()
obj_2 = Akbar()
obj_3 = Anthony()
obj_1.BHK1()
obj_1.BHK2()
obj_3.BHK()