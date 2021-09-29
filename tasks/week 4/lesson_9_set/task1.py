# На входе функция to_set() получает строку или список чисел.
# Преобразуйте их в множество. На выходе должно получиться множество иx сумма.

def to_set(lists):
    new_set = set(lists)
    return new_set, len(new_set)

list1 = [3, 6, 4, 9, 4]
list2 = ['h', 'e', 'l', 'l', '0', ' ']
print(to_set(list1))
print(to_set(list2))