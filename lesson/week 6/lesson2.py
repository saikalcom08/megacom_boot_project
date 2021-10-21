# НАСЛЕДОВАНИЕ
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.staj = 0
#
#     def work(self):
#         print(f"{self.name} working")
#
#     def eat(self):
#         print(f"{self.name} eating")
#
#     def walk(self):
#         print(f"{self.name} walking")
#
#     def breath(self):
#         print(f"{self.name} breathing")
#
#     def combo(self):
#         self.breath()
#         self.eat()
#         self.work()
#         self.walk()
#         if hasattr(self, "treat"):
#             self.treat()
#
# class Doctor(Person):
#     def work(self):
#         self.staj += 1
#         print("doctor works 24 hours", self.staj)
#
#
# class Ortoped(Doctor):
#     def treat(self):
#         print(f"{self.name} treating")
#
# john = Doctor("John", 45)
# stephen = Ortoped("Stephen", 35)
# # john.work()
# # john.work()
# # john.work()
# # stephen.work()
# # stephen.work()
# # john.breath()
#
# stephen.combo()
# john.combo()
# # print(hasattr(treat, Ortoped))
# ==============================================
# class Country:
#     def __init__(self, population):
#         self.population = population
#
#     def setPopulation(self, population):
#         self.population += population
#         return self.population
#
#     def getPopulation(self):
#         return self.population
#
# class Russia(Country):
#     pass
# class Canada(Country):
#     pass
#
# class Germany(Country):
#     pass
#
# canada = Canada(400000000)
# print(canada.getPopulation())
# print(canada.setPopulation(-458963))
# print(canada.population)
# =============================================
class Maths:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

summa = Maths(7, 8)
print(summa.get_sum())