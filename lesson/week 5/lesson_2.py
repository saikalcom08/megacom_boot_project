# isinstance
# print(isinstance(4, int)) # TRUE
# print(isinstance(4, int)) #FALSE
#==============================================================
# class Dog:
#     poroda = "Alabai"
#
# a = Dog()
# b = Dog()
# a.poroda = "Avcharka"
# del a.poroda
# b.size = "big"
# # print(isinstance(a, Dog))
# print(a.poroda)
# print(b.poroda)
# print(a.__dict__)
# print(b.__dict__)
# # print(Dog.__dict__)
#===============================================================
# class Car:
#     model = "Mers"
#     year = 1999

#     def get_info_car(self, probeg, name, price):
#         self.name = name
#         self.probeg = probeg
#         self.price = price
#         print(f"Машина {self.name} имеет {self.probeg}, цена-{self.price} год выпуска: {self.year}")
#
# car1 = Car()
# car1.get_info_car(2000, "mers c class", 45000000)
# print(car1.__dict__)
#=================================================================
# class Car:
#     model = "mashina"
#
#     def __init__(self, name, year, price):
#         self.name = name
#         self.year = year
#         self.price = price
#         self.probeg = 0
#
#     def drive(self, km):
#         self.probeg = self.probeg + km
#         return self.probeg
#
# mers = Car("Mersedes S class", 1999, 45000000)
# toyota = Car("Rav4", 2009, 100000000)
#
# mers.drive(40)
# mers.drive(1000)
# toyota.drive(100)
# print(mers.probeg)
# print(toyota.probeg)
#====================================================
import math
class Triangle:

    def __init__(self, a = 42, b = 45, c = 90):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        return round((math.sqrt(semi_perimeter * (semi_perimeter-self.a)*(semi_perimeter-self.b)*(semi_perimeter-self.c))), 1)
    def perimeter(self):
        return self.a + self.b + self.c
    def summa(self):
        summa = self.area() + self.perimeter()
        return summa

triangle1 = Triangle(7, 9, 4)
print(f"area = {triangle1.area()}")
print(f"perimeter = {triangle1.perimeter()}")
print(f"summa = {triangle1.summa()}")
