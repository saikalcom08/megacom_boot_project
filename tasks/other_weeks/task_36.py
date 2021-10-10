# Создать функцию calc(a, b, operation).
# Описание входных параметров:
#   1. Первое число
#   2. Второе число
# 3. Действие над ними:
#     1) + Сложить
#     2) - Вычесть
#     3) * Умножить
#     4) / Разделить
#     5) В остальных случаях функция должна возвращать "Операция не поддерживается

def calc(a, b, operation):
    if operation == '+':
        summa = a + b
    if operation == '-':
        summa = a - b
    if operation == '*':
        summa = a * b
    if operation == '/':
        summa = a / b
    else:
        print("there is no such operation: ")
    print(summa)

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
operation = input("enter operation (+, -, *, /): ")

calc(a, b, operation)