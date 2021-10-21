# classmethod, staticmethod, instancemethod
from datetime import datetime
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_instance_info(self):
        return self.name, self.age

    @classmethod
    def get_class_info(cls, name, year):
        # return cls(name, datetime.now().year - year)
        return name, datetime.now().year - year

    @staticmethod
    def get_static_info():
        print("Privet")

kiyal = Person("Kiyal", 19)
saikal = Person.get_class_info("Saikal", 1990)
print(kiyal.get_instance_info())
print(kiyal.name)
print(saikal)
#print(saikal.name)
#print(saikal.age)
a = Person("name", 23)
a.get_static_info()
Person.get_static_info()


