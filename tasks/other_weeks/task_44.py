# Возьмите массив и удалите из него каждый второй элемент.
# Всегда сохраняйте первый элемент и начинайте удаление со следующего элемента.
# Пример:
# ["Keep", "Remove", "Keep", "Remove", "Keep"] --> ["Keep", "Keep", "Keep"]

def removing(lists):
    del lists[1::2]
    return lists

lists = ["Keep", "Remove", "Keep", "Remove", "Keep"]
print(removing(lists))