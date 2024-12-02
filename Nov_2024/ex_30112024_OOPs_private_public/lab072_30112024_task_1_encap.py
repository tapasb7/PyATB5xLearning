# Create a class, with
# public and private variables and
# method to access them outside

class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # public variable
        self.age = age # public variable
        self.__salary = salary  # private variable (double underscore)

    def get_age(self):  # public method to access protected variable
        return self.age

    def get_salary(self):  # public method to access private variable
        return self.__salary



# create an instance of the Employee class
emp = Employee("Michael Jakson", 35, 50000)

# access public variable
print(emp.name)  # Output: Michael Jakson

# access protected variable using public method
print(emp.get_age())  # Output: 35

# access private variable using public method
print(emp.get_salary())  # Output: 50000

# access private variable directly (not recommended)
# print(emp.__salary)  # Raises AttributeError

