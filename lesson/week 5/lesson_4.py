# Принцип программирования Инкапсуляция

class Bank:
    def __init__(self, name, age, inn, money):
        self.name = name
        self.age = age
        self.__inn = inn
        self.__money = money
    # def get_inn(self):
    #     print(self.__inn)
    #
    # def get_money(self):
    #     print(self.__money)
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, new_money):
        self.__money = new_money
        # return self.__money

    @money.deleter
    def money(self):
        del self.__money

baitik = Bank("Baitik", 17, "122222222221", 1000000)
# baitik.get_inn()
# print(baitik.__inn)
# print(dir(Bank))
# print(baitik._Bank__inn)
baitik.money = 3
del baitik.money
print(baitik.money)
