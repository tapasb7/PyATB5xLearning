class Father:

    def father_money(self):
        return 10

    def home(self):
        print("Father Home")


class Mother:
    def mother_money(self):
        return 15
    def home(self):
        print("Mother Home")

class Son(Father,Mother):
    def print_info(self):
        print("Son")


Ranveer = Son()
print(Ranveer.father_money())
print(Ranveer.mother_money())
Ranveer.home() #In case of same function_name it will pick first one