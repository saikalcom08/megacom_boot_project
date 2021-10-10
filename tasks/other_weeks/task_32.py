# Создать программу, которая будет переводить число в римские и выводить на экран. Значение числа до 100.
num = 89
result = ''
# 90 -> 9
# 91 -> 1
if num == 100:
    result = 'C'
elif 0 < num < 100:
    # десятки
    a = num // 10
    if a == 9:
        result += 'XC'
    elif a == 8:
        result += 'LXXX'
    # единицы
    b = num % 10
    if b == 9:
        result += 'IX'
print(result)