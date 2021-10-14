# моносостояние
# class Dog:
#     poroda = "Alabai"
#     size = "big"
#
# print(Dog.__dict__)
# dog1 = Dog()
# dog1.year = 3
# print(dog1.__dict__)
# =====================================================
# class Dog:
#     __mono_attr = {"poroda": "Alabai", "size": "big"}
#
#     def __init__(self):
#         self.__dict__ = Dog.__mono_attr
#
# alabai = Dog()
# bulldog = Dog()
# bulldog.age = 4
# print(alabai.poroda)
# print(alabai.size)
# print(bulldog.poroda)
# print(bulldog.size)
# print(bulldog.age)
# print("\n")
# alabai.poroda = "Avcharka"
# print(alabai.poroda)
# print(alabai.size)
# print(bulldog.poroda)
# print(bulldog.size)
# print(bulldog.age)
# ================================================
class Student:
    def __init__(self, name, group, age, kpi):
        self.name = name
        self.group = group
        self.age = age
        self.kpi = kpi
    def get_kpi(self):
        counter = 0
        for item in self.kpi.values():
            counter += item
        return counter/len(self.kpi)
    def get_info(self):
        lists = []
        for item in self.kpi:
            lists.append(item)
            x = ", ".join(lists)
        print(f"{self.name} учиться в группе {self.group}, ей {self.age} лет. Она учит {x} предметы")

meerim_dict = {
    "алгебра" : 100,
    "химия": 80,
    "физ-ра": 100,
    "биология": 60
}
kyal_dict = {
    "алгебра": 90,
    "химия": 80,
    "физ-ра": 95,
    "биология": 60
}
meerim = Student("Meerim", "python_bootcamp", 18, meerim_dict)
kyal = Student("Kyal", "python_bootcamp", 25, kyal_dict)
print(meerim.get_kpi())
print(kyal.get_kpi())
kyal.get_info()
meerim.get_info()