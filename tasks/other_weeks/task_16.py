# Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

a = int(input("первое число: "))
b = int(input("второе число: "))
p = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
nod = a + b
nok = p // nod
print ('НОК введённых чисел:', nok)