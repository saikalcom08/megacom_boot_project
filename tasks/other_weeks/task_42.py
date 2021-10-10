# Напишите функцию, которая удваивает каждое второе целое число в списке, начиная слева.
# Пример:
# double_every_other([1,2,3,4]) ->> [1, 4, 3, 8]

def double_every_other(lists):
    for i in range(1, len(lists), 2):
        lists[i] *= 2
    return lists
lists = [10, 8 ,3 ,4]
print(double_every_other(lists))
