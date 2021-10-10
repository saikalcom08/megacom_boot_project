# Проверить трехзначное число на четность и найти сумму его цифр,
# если число четное, или произведение его цифр, если число нечетное.

number = int(input("Введите 3-х значное число: "))
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

if number % 2 != 0:
	print("Число нечетное. Произведение цифр:", hundreds * tens * ones)
else:
	print("Число четное. Сумма цифр:", hundreds + tens + ones)
