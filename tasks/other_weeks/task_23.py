# Угадать число, которое загадал пользователь, используя только инструкцию if-else.
import random
number = random.randrange(1, 11)
counter = 0
while counter < 3:
    x = int(input("Введите число от 1 до 10:"))
    if x == number:
        print("Угадали!")
        break
    else:
        print("Не угадали")
    counter += 1
