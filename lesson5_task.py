#1.Список, состоящий из квадратов s.
def filling_squares():
    lists = [pow(x, 2) for x in range(1, 10)]
    print(lists)

#2.Список, состоящий из остатков деления на 11 элементов s.
def remainder():
    lists = [x % 11 for x in range(1, 10)]
    print(lists)

#3.Список, состоящий только из чётных элементов s.
def even_number():
    lists = [x for x in range(1, 10) if x % 2 == 0]
    print(lists)

#4.Список, состоящий только из элементов s с нечётным количеством цифр.
def odd_number():
    lists = [x for x in range(1, 10) if x % 2 != 0]
    print(lists)

#5.Список, состоящий только из двухзначных элементов s, записанных 2 раза подряд.
def duplicated_numbers():
    lists = [x for x in range(1, 1000) if len(str(x)) == 2 and str(x)[0] == str(x)[1]]
    print(lists)

#6.Список, состоящий из элементов s, стоящих на позициях, не кратных 3.
def not_divided_by_three():
    lists = [x for x in range(10, 20)]
    result = [x for x in range(len(lists)) if lists[x] % 3 != 0]
    for i in result:
        print(lists[i])

filling_squares()
remainder()
even_number()
odd_number()
duplicated_numbers()
not_divided_by_three()