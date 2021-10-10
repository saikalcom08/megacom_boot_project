# Написать программу, которая находит все комбинации из трех чисел до определенного предела,
# которые в сумме дают другое число. Предел трех чисел и заданное число-сумму вводить с клавиатуры.

number = int(input('Предел для перебираемых чисел: '))
summa_enter = int(input('Искомая сумма: '))

for i in range(1, number+1):
    for j in range(1, number+1):
        for k in range(1, number+1):
            summa = int(i) + int(j) + int(k)
            if summa == summa_enter:
                print(f"{i} {j} {k}")