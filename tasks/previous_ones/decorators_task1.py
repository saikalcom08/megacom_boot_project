#1. Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
#В результате ее работы на печать в консоль выводятся значения переданных переменных,
# но только если они не равны None.
#Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».

def three_args(var1, var2, var3):
    if (var1 and var2 and var3) and (0 in (var1, var2, var3)):
        print('var1 = {}, var2 = {}, var3 = {}'.format(var1, var2, var3))
    else:
        print("You attempted an empty entrance")
    return var1, var2, var3

input1 = input("variable 1:")
input2 = input("variable 2:")
input3 = input("variable 3:")
three_args(input1, input2, input3)
