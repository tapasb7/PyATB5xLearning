class Father:
    flat_1 = "2BHK"
    car_1 = "Alto"

    def father_wealth(self):
        print(f"Father has a {self.car_1} and a {self.flat_1} ")

class Son(Father):   # Son class can inherit all attributes & methods from "Father" class
    flat_2 = "3BHK"
    car_2 = "Alto"

    def son_wealth(self):
        print(f"Son has {self.car_2} and {self.flat_2}")


Ramesh = Son()
print(Ramesh.father_wealth())