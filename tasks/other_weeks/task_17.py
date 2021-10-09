# Ввести число в консоли. Проверить , что если число меньше 10 ,
# то оно делиться на оно нацело на 2, если число в промежутке между 10 и 100,
# то проверить делится ли нацело на 3, если число больше 100, то проверить делится ли нацело на 4.
# Вывести True или False

number = int(input("введите число: "))
if number < 10 and number % 2 == 0:
    print(True)
elif 10 <= number < 100 and number % 3 == 0:
    print(True)
elif number >= 100 and number % 4 == 0:
    print(True)
else:
    print(False)