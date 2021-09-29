#Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе.
#Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.
import random
def generator_random_number(func):
    def wrapper(*args):
        random_lists = [random.randint(10, 50) for x in range(100)]
        res = func(random_lists)
        return res
    return wrapper

@generator_random_number
def del_duplicates(lists):
    return list(dict.fromkeys(lists))

lists = []
print(del_duplicates(lists))

