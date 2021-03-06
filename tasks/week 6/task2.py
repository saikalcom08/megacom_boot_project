# Определить класс Car с полями название, цвет, цена, const полем CompanyName.
# Создать  конструктор - дефолтный и с параметрами. Создать свойство доступа к полю цвет.
# Определить методы Input () - для ввода данных о машине с консоли ,
# Print () - для вывода данных о машине на консоль и
# ChangePrice (double x) - для изменения цены на х%
# Ввести данные о 3 авто.
# Уменьшить их цену на 10%,
# вывести данные об авто.
# Ввести новый цвет и покрасить авто с цветом white в указанный цвет

class Car:
    COMPANY_NAME = "Saikal and Co"
    def __init__(self, name = "Jeep", color = "black", price = 45000):
        self.name = name
        self.color = color
        self.__price = price

    def input_from_console(self):
        self.name = input("Enter car name: ")
        self.color = input("Enter color of the car: ")
        self.__price = int(input("Enter price of the car: "))
        return self.name, self.color, self.__price

    def print_from_console(self):
        print(f"Your car name: {self.name}, your car color: {self.color}, car price: {self.__price}")

    def change_price(self, percentage):
        res = (percentage * self.__price) / 100
        self.__price -= res
        return self.__price

car1 = Car() # BMW, black, 78000
car2 = Car() # Lamborghini, white, 100000
car3 = Car() # Toyota, grey, 90000

lists = [car1, car2, car3]
for index in lists:
    index.input_from_console()
    index.print_from_console()
    print("Price after discount")
    index.change_price(10)
    index.print_from_console()

new_color = input("Enter color to dye: ")
car1.color = new_color
car1.print_from_console()


