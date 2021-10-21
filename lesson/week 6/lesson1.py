# полиморфизм
# class Dog:
#     def __init__(self, name, poroda, age):
#         self.name = name
#         self.poroda = poroda
#         self.age = age
#
#     def get_sound(self):
#         print(f"{self.name}, гав гав")
#
#     def get_eat(self):
#         print(f"{self.name}, ням ням")
#
#
# class Cat:
#     def __init__(self, name, poroda, age):
#         self.name = name
#         self.poroda = poroda
#         self.age = age
#
#     def get_sound(self):
#         print(f"{self.name}, мяу мяу")
#
#     def get_eat(self):
#         print(f"{self.name}, белиссимо")
#
# rex = Dog("Rex", "avcharka", 3)
# cat1 = Cat("Caty", "bengal", 2)
# cat2 = Cat("Caties", "bengal", 4)
#
# # rex.get_sound()
# # cat1.get_sound()
# lists = [rex, cat1, cat2]
# for i in lists:
#     print(i.age)
#     i.get_sound()
#     i.get_eat()

# ===================================
class Cash:
    def __init__(self, name, total_money):
        self.total_money = total_money

    def __add__(self, other):
        if isinstance(other, Cash):
            return int(self.total_money) + int(other.total_money)
        if type(self.total_money) == str:
            return int(self.total_money) + other

    def __mul__(self, other):
        if isinstance(other, Cash):
            return int(self.total_money) * int(other.total_money)
        if type(self.total_money) == str:
            return int(self.total_money) * other

    def __sub__(self, other):
        if isinstance(other, Cash):
            return int(self.total_money) - int(other.total_money)
        if type(self.total_money) == str:
            return int(self.total_money) - other

    def __truediv__(self, other):
        if isinstance(other, Cash):
            return int(self.total_money) / int(other.total_money)
        if type(self.total_money) == str:
            return int(self.total_money) / other

    def __radd__(self, other):
        print("вызов rad addition")
        return self + other

    def __rmul__(self, other):
        print("вызов rad multiply")
        return self * other

    def __rsub__(self, other):
        print("вызов rad subtraction")
        return other - self

    def __rtruediv__(self, other):
        print("вызов rad division")
        return self / other

nazgul = Cash("Nazgul", '8')
meerim = Cash("Meerim", '2')
print(nazgul + meerim) # 2 + 8 = 10
print(nazgul + 25) # 2 + 25 = 27
print(25 + meerim) # 25 + 8 = 33
print("Multiply: ")
print(nazgul * meerim) # 2 * 8 = 16
print(nazgul * 4) # 2 * 4 = 8
print(4 * nazgul) # 4 * 2 = 8
print("Subtraction: ")
print(nazgul - meerim) # 8 - 2 = 6
print(nazgul - 10) # 8 - 10 = -2
print(10 - nazgul) # 10 - 8 = 2
print("Division: ")
print(nazgul / meerim) # 2/8 = 4.0
print(nazgul / 10) # 8/10 = 0.8
print(10 / nazgul) # 10/8 = 0.8
# __sub__, __trudiv__