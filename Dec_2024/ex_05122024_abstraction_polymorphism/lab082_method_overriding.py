# same method name but different form

class Parent:

    def home(self):
        print("2BHK")

class Child(Parent):

    def home(self):  #home method is overriding here
        print("3BHK")

    def

obj_1 = Child()
obj_1.home()