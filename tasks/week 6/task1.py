# Создать класс Money для работы с денежными суммами в котором для рублей и копеек
# предусмотрены независимые целочисленные данные. Реализовать метод вывода суммы на экран.
# На основе класса Money создать класс Good для работы с товаром.
# Предусмотреть метод, осуществляющий уменьшение цены на заданное число процентов.

class Money:

    def get_money(self):
        rub = int((self.money * 100) // 100)
        kop = int(round(((self.money - rub) * 10), 0))
        return f"{rub} rublei {kop} kopeek"

class Good(Money):

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def discount(self, percentage):
        self.money = self.money * (100-percentage)/100
        return self.money

pen = Good("Pen", 25.5)
print(f"tsena tovara do skidki: {pen.get_money()}")
pen.discount(15)
print(f"vash tovar posle skidki: {pen.get_money()}")
