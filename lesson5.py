#генераторы списков

#lists = []
# for i in range(0, 100):
#     lists.append(i)
# print(lists)
#====================================
# list2 = [x for x in range(100)]
# print(list2)
#====================================
# list3 = []
# for i in range(0, 1000):
#     if i % 3 == 0:
#         list3.append(i)
# print(list3)
#===================================
# list4 = [x for x in range(1, 100) if x % 3 == 0]
# print(list4)
#===================================
# list5 = []
# for i in range(-100, 50):
#     if i%3 == 0 and i%5 == 0:
#         number = pow(i,3)
#         #number = abs(i**3)
#         list5.append(number)
# print(list5)
#===================================
# list5 = [pow(x, 3) for x in range(-100, 50) if (x % 3 == 0 and x % 5 == 0)]
# print(list5)
# ===================================
# def filter_number(range1, range2):
#     list5 = [pow(x, 3) for x in range(range1, range2) if (x % 3 == 0 and x % 5 == 0)]
#     return list5
# list1 = filter_number(-100,200)
# print(list1)
# ===================================
kyal = {
    'home': '2floor',
    'car': 'BMW x7'
}
saikal = {
    'home': '3floor',
    'car': 'Toyota 470'
}
eldar = {
    'home': '6floor',
    'car': 'Mers 222'
}
#print(python_boot[i].get('home'))
# python_boot = [eldar, saikal, kyal]
# home = list()
# for i in python_boot:
#     home.append(i.get('home'))
#
# print(home)
# =====================================
# python_boot = [eldar, saikal, kyal]
# car = [x.get('car') for x in python_boot]
# print(car)
#======================================
from datetime import datetime

def func1():
    lists = []
    start_time = datetime.now()
    for i in range(1, 100000):
        lists.append(i)
    end_time = datetime.now() - start_time
    print('time for for loop: ', end_time)
    return lists

def func2():

    start_time = datetime.now()
    lists = [x for x in range(1, 100000)]
    end_time = datetime.now() - start_time
    print('time for list comprehensions: ', end_time)
    return lists

func1()
func2()
#==========================================