class dog:
    # Attributes
    name = None
    breed = None
    color = None
    weight = None

    # init function
    # def __init__(self):
    #     print("This is constructor function")
    def __init__(self, name, color):
        print("PC")
        self.name = name
        self.color = color

    # Behaviour
    def sleep(self):
        print(self.color, " dog is Sleeping. Its name is ", self.name)

    def bark(self):
        print(self.color, " dog is Barking. Its name is ", self.name)

    def eat(self):
        print("Eating")


# obj reference (create an object of the class)
dog_1 = dog("Chow", "Brown")
# dog_1.name = "Chow"
dog_2 = dog("Kallu", "Black")
# dog_3 = dog()


dog_1.sleep()
dog_2.bark()

print(id(dog_2))
print(id(dog_1))
