class Human:
    default_name = "No name"
    default_age = 0
    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None


    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Money : {self.__money}")
        print(f"House : {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned {amount} money! Current value: {self.__money}")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("You can buy this house!")
        else:
            print("Not enough money!")

class House:
    def __init__(self, area=45, price=35000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        res = self._price * (100 - discount)/100
        print(f"Final price: {res}")
        return res


saikal = Human("Saikal", 31)
saikal.info()
Human.default_info()
saikal.earn_money(90000)
saikal.info()

house = House(45, 15000)
saikal.buy_house(house, 5)