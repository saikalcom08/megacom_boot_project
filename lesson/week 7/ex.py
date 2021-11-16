# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#
#     def get_gender(self, gender):
#         if gender == 'male':
#             return gender
#         elif gender == 'female':
#             return gender
#
# gender = input("Enter gender: ")
# person = Person('Saikal', 'Esenturova', gender)
# if person.get_gender(gender):
#     print(f"Гражданка {person.name}{person.surname}{person.gender}")
# else: print("error")

class Foo (object):
    x = 1
    _x_ = 2
    __x__ = 3

print(Foo.x, Foo._x_, Foo.__x__)