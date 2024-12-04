# Multilevel
class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")


Neil = Son()
Nitin = Father()
Mukesh = GrandFather()
print(Neil.gold)
# print(Mukesh.btc) Mukesh can't access btc as it belongs to Son class
