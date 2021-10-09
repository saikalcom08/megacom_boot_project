# class MyClass:
#     variable = "blah"
#     def function(self):
#         print("This is a message inside the class.")
# myobjectx = MyClass()
# print(myobjectx)
#========================================================
# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
#
# print(myobjectx.variable)
#==========================================================
# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
# myobjecty = MyClass()
#
# myobjecty.variable = "yackity"
#
# # Then print out both values
# print(myobjectx.variable)
# print(myobjecty.variable)
#==================================================
# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
#
# myobjectx.function()
#=============================================
# define the Vehicle class
# class Vehicle:
#     name = "Lamborgini"
#     kind = "car"
#     color = "pink"
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# your code goes here
# car1 = Vehicle()
# car2 = Vehicle()
#
# car2.name = "BWW"
# car2.kind = "car"
# car2.color = "yellow"
# car2.value = 1000.0
# # test code
# print(car1.description())
# print(car2.description())

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)