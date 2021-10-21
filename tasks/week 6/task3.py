class Product:
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    def get_price(self):
        return self._price

    def get_weight(self):
        return self._weight

    def show_goods(self):
        print(f"Good name: {self._name}\n price: {self._price}\n weight: {self._weight}")

class Buy(Product):
    def __init__(self, price, weight):
        super().__init__(price, weight)
        self._quantity = 10

    def calculate_total(self, ):
        temp1 = super().get_price()
        temp2 = super().get_weight()
        total_price = temp1 * self._quantity
        total_weight = temp2 * self._quantity
        print(f"Goods bought: {self._quantity}\n Total price: {total_price}\n Total weight: {total_weight}")

class Check(Buy):
    product = Product("Ice cream", 20, 500)
    product.show_goods()
    buy = Buy()
    buy.calculate_total()


check = Check()
