# Написать программу, подсчитывающую количество четных и нечетных цифр в числе.

number = input("Введите любое число: ")
countEven = 0
countOdd = 0
for i in number:
    if int(i) % 2 == 0:
        countEven += 1
    if int(i) % 2 != 0:
        countOdd += 1
print(countEven, "even numbers")
print(countOdd, "odd numbers")