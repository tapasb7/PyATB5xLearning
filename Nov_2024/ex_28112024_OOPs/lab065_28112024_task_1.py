# Task 1 - Create a Class PyATB ,
# 5 Attributes, 3 Functions/Methods

class PyATB:
    name = None
    contact = None
    address = None
    batch = None
    experience = None

    def __init__(self, name, contact, address, batch, experience):
        self.name = name
        self.contact = contact
        self.address = address
        self.batch = batch
        self.experience = experience

    def show_name(self):
        print("Name of the student is : ", self.name)

    def show_batch(self):
        print("batch : ", self)

    def show_contact(self):
        print()


student_1 = PyATB("Sudarshan", "8431488447", "Bangalore", "PyATB5x", 10)
student_2 = PyATB("Vishma", "9874589554", "New Delhi", "PyATB5x", 3)
student_3 = PyATB("Arjun", "7432557895", "Gowalior", "PyATB5x", 5)

student_1.show_name()

