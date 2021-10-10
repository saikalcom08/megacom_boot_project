# Напишите программу, которая будет принимать ключ X и помещать его в середину Y, повторяемую N раз
# Правила:
# Если X не может быть помещен в середину, верните X.
# N всегда будет> 0.
# Пример:
# X = 'A'
# Y = '*'
# N = 10
# Y повторяется N раз = '**********';
# X в середине Y повторяется N раз = '*****A*****'
y = input("Enter symbol: ")
n = int(input("How many times should repeat: "))
x = "A"

res = y * n
if len(res) % 2 == 0:
    index = len(res) // 2
    res = res[:index] + x + res[index:]
    print(res)
else:
    print(x)