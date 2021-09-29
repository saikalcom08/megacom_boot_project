#встроенные функции
# def x(a): #parametr
#     return a
#
# print(x(4)) # argument

#===================================
#map, filter, reduce

# list1 = [2, 3, 4, 5, 8, 10, 12]
# list2 = [pow(x,2) for x in list1]
# print(list2)

#=====================================
#MAP
# list1 = [2, 3, 4, 5, 8, 10, 12]
# def square(num):
#     return num**2
#
# list3 = list(map(square, list1))
# print(list3)
#=====================================
# names = ['meerim', 'saikal', 'kyial']
#
# def title(str):
#     return str.title()
#
# name_list = list(map(title, names))
# print(name_list)
#=====================================
# phone_numbers = ['0 996 44 33 22', '0 996 707 55 66 44', '0 996 700 09 09 62']
#
# def replace(number):
#     return number.replace(' ', '-')
#
# changed_numbers = list(map(replace, phone_numbers))
# print(changed_numbers)
#=======================================
#FILTER
# numbers = [4, 5, 8, 12, 34, 7]
#
# def oddNumbers(num):
#     if num % 2 != 0:
#         return num
#
# new_numbers = list(filter(oddNumbers, numbers))
# print (new_numbers)
#=======================================

# x= 'saykal'
# if x.startswith('say'): #endwith()
#     print(True)
# else:
#     print(False)
#=======================================
# country = ['Kyrgyzstan', 'Russia', 'China', 'Kazakstan']
# def k_country(country):
#     if country.startswith("K"):
#         return True
#
# country_k = list(filter(k_country, country))
# print(country_k)
#========================================
# kpi = [100, 150, 99, 88, 70, 66, 200]
#
# def define_student_fail(num):
#     if num < 80:
#         return 'fail: ', num
#
# def define_student_pass(num):
#     if num > 100:
#         return 'pass: ', num
#
# new_kpi_fail = list(filter(define_student_fail, kpi))
# new_kpi_pass = list(filter(define_student_pass, kpi))
# print("failed kpi: {} \npassed kpi: {}".format(new_kpi_fail, new_kpi_pass))

#=========================================
#REDUCE
from functools import reduce
# def multiply(x, y):
#     return x * y
#
# numbers = [2, 4, 9, 5, 3]
# mult = reduce(multiply, numbers)
# print(mult)
#==========================================
# def concatination(str1, str2):
#     return str1+str2
#
# letters = ['m', 'e', 'e', 'r', 'i', 'm']
# word = reduce(concatination, letters)
# print(word)

#========================================
#LAMBDA
# letters = ['m', 'e', 'e', 'r', 'i', 'm']
# word = reduce(lambda x, y: x + y, letters)
# print(word)
#========================================
# numbers = [2, 3, 5, 8, 1]
# lists = list(map(lambda x: x**2, numbers))
# print(lists)
#=======================================