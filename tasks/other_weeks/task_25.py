# Создать тест из 10 вопросов. В каждом вопросе рандомно выбирать 2 числа от 2 до 9. Отобразить в виде 7 * 3 =.
# Пользователь далее должен ввести правильный ответ.
# В конце теста вывести процент правильных ответов.
#
# 1. 7 * 4 =
# 2. ...
# 3. ...
# Ваш результат: 80%
import random
count_plus = 0
count_minus = 0
count_answer = 0
for i in range(0, 10):
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    answer = int(input(f"{number1} x {number2} = "))
    if answer == number1 * number2:
        count_plus += 1
    else:
        count_minus += 1
print("correct answers: ", count_plus)
print("incorrect answers: ", count_minus)
result = round(((100 * count_plus) / 10), 1)
print(result,"%")
