# Число делится на 6 только в случае соблюдения двух условий: последняя его цифра четная, а сумма всех цифр делится на 3.
#
# Вывести на экран True или False
# Ввести число в консоли.

number = int(input("Enter number: "))
last_str_digits = list(str(abs(number)))
last_digits = list(map(int, last_str_digits))
sum_digits = sum(last_digits)
if (sum_digits % 3 == 0) and (lst_digits[-1] % 2 == 0):
    print(f'Число {number} делится на 6')
else:
    print(f'Число {number} неделимо на 6')