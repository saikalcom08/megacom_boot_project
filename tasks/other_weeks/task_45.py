# Создать 2 списка.
# Создать функцию, которая будет заполнять их случайными числами от 1 до 10
# Добавить в третий список повторяющиеся числа
# Добавить в четвертый список числа из первого списка, которые отсутствуют во втором

import random
def random_numbers(list1, list2):
    list3 = [i for i, j in zip(list1, list2) if i == j]
    list4 = [i for i in list1 if i not in list2]
    return "repeating numbers: ", list3, "difference: ", list4
list1 = [random.randrange(1, 10) for i in range(7)]
print("list1: ", list1)
list2 = [random.randrange(1, 10) for i in range(7)]
print("list2: ", list2)
print(random_numbers(list1, list2))