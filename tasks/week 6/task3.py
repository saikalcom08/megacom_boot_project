class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def show_goods(self):
        print(f"Good name: {self.__name}\n price: {self.__price}\n weight: {self.__weight}")

class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity

    def calculate_total(self, ):
        temp1 = super().get_price()
        temp2 = super().get_weight()
        total_price = temp1 * self.__quantity
        total_weight = temp2 * self.__quantity
        print(f"Goods bought: {self.__quantity}\n Total price: {total_price}\n Total weight: {total_weight}")

class Check(Buy):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight, quantity)

check = Check("Ice cream", 20, 500, 3)
check.show_goods()
check.calculate_total()
