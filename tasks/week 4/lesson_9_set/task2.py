# Имеется список с произвольными данными. Поставлена задача преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Функция list_to_set() выводит на печать получившееся множество.

# x = hash(set([1,2])) #set unhashable
# x = hash(frozenset([1,2])) #hashable
# x = hash(([1,2], [2,3])) #tuple of mutable objects, unhashable
# x = hash((1,2,3)) #tuple of immutable objects, hashable
# x = hash()
# x = hash({1,2}) #list of mutable objects, unhashable
# x = hash([1,2,3]) #list of immutable objects, unhashable

# Список неизменяемых типов:
# int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

# Список изменяемых типов:
# list, dict, set, bytearray, user-defined classes

# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# x = isinstance(5, int) => TRUE

from collections.abc import Hashable

def check_hashable(lists):
    example = {elem for elem in lists if isinstance(elem, Hashable)}
    print(example)

check_hashable([[1,2], [2], (1,2,3)])
check_hashable(['i am string', {1, 2}, [1, 2, 3], 0.4, {1, 2, 3}, (2, 2), 9])