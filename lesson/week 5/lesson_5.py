# вычисляемые свойства проперти

# class Circle:
#
#     def __init__(self, r):
#         self.__r = r
#         self.__area = None
#     @property
#     def radius(self):
#         return self.__r
#
#     @radius.setter
#     def radius(self, rad):
#         self.__r = rad
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             self.__area = self.__r**2 * 2 * 3.14
#         return self.__area
#
# circle1 = Circle(34)
# print(circle1.area, "before")
# circle1.radius = 5
# print(circle1.radius)
# print(circle1.area, "after")
# print(circle1._Circle__area, "__area")
# =============================================
class Circle:

    def __init__(self, r, name):
        self.name = name
        self.__r = r
        self.__area = None

    def __str__(self): #строковое представление объекта
        #return f"object from Circle with radius {self.__r}"
        return f"object from Circle with radius {self.name}"

a = Circle(4, "Baitik")
b = Circle(3, "Eldar")
print(a)
print(b)
