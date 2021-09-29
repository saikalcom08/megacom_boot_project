# Найти (row, col) элемента х в матрице (списке списков).
# Если  элемента х нет, то возбудить исключение ValueError.
# Использовать  метод списка index. И обработать.

twodim_lists = [[5, 4, 7, "y"], ["a", 2, 8, "s"]]
elem = "v"
new_list = []
for item in twodim_lists:
    new_list.append(item[0])
print(new_list)
try:
    result = new_list.index(elem)
    print('SUCCESS. There is {} in given list'.format(elem))
except ValueError:
    print('ERROR. There is NO {} in given list'.format(elem))
