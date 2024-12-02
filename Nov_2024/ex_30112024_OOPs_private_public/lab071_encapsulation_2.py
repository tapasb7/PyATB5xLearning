class bank():
    def __init__(self, ac_num, balance):
        self.balance = balance
        self.__ac_num = ac_num          #private variable

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_ac_num(self):
        print(self.__ac_num)

icici_bank = bank(76899897612, 100)
print(icici_bank.balance)
icici_bank.deposit(120)
icici_bank.check_balance()
# print(icici_bank.ac_num)
# #can not access ac_num because it is encapsulated private variable
icici_bank.check_ac_num() #only a function can access the private variable


