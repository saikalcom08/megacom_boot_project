#decorators
# from datetime import datetime
#
# def time(func):
#     def wrapper():
#         start_time = datetime.now()
#         func()
#         end_time = datetime.now() - start_time
#         print(end_time)
#     return wrapper
#
# @time
# def func1():
#     lists = []
#     for i in range(1, 100000):
#         lists.append(i)
#     return lists
#
# @time
# def func2():
#     lists = [x for x in range(1, 100000)]
#     return lists
#
# func1()
# func2()

#================================================

# def hamburger(cotlet):
#     def wrapper():
#         print("верхняя булочка")
#         print("верхний салат")
#         print("кетчуп, майонез")
#         cotlet()
#         print("нижний салат")
#         print("нижняя булочка")
#     return wrapper
#
# @hamburger
# def cotlet_beef():
#     print('beef')
#
# @hamburger
# def cotlet_lamb():
#     print('lamb')
#
# @hamburger
# def cotlet_chicken():
#     print('chicken')
#
# cotlet_beef()

#=========================================

# def hamburger(cotlet):
#     def wrapper(*args, **kwargs):
#         print("верхняя булочка")
#         cotlet(*args, **kwargs)
#         print("нижняя булочка")
#     return wrapper
#
# @hamburger
# def cotlet(ingredients):
#     #print(f"котлета из {ingredients}")
#     print("котлета из {}".format(ingredients))
#     return
#
# cotlet("chicken")

#==========================================

# lists = ["Kyal", "Saikal", "Meerim", "Iskender"]
# print(f"m-{lists[1]}-{lists[2]}")
# print("{0} {2} {1} {3}".format(lists[1], lists[3], lists[0], lists[2])) # orientir vnutri karteja

#=============================================

#======== VSTROENNAIA (BUILT-IN) FUNCTION ===============

# d = {
#     "name": "Vika",
#     "age": 18
#     }
#
# name = d.pop("name")
# d.update({"name": "Eldar"})
# print(len(d)) # this is function , function is independent
# print(d) # this is method, method is dependable (t.e tochka i vyzyvaetsia)
#print(name)

#==========================================
import math
# pow()
# len()
# abs()
# round()
# sqrt() # this is taken from math
# sum()
# max()
# min()
# print(pow(3, 2)) #stepen'
# print(math.sqrt(4))

#==========================================
# def factorial(n):
#     count = 1
#     for x in range(1, n+1):
#         count *= x
#     return count
#
# number = int(input("enter a number:"))
# print(factorial(number))

#=========================================
def pifagor(a,b):
    c = pow(a,2) + pow(b,2)
    c = math.sqrt(c)
    return c

katet1 = int(input("enter katet 1: "))
katet2 = int(input("enter katet 2: "))
print(pifagor(katet1, katet2))
