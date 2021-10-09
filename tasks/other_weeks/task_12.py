# Должен знать либо python, либо java, либо javascript.
# Возраст от 18 до 65. Опыт от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или нет.
#
# Язык программирования:
# Возраст:
# Опыт:
# Желаемая зарплата:

language = input("Язык программирования: ").lower()
age = int(input("Возраст: "))
experience = int(input("Опыт: "))
salary = int(input("Желаемая зарплата: "))

if language in ["python", "java", "javascript"] and (18 <= age <= 65) and (experience >= 3) and (salary <= 60000):
    print("You are eligible!")
else:
    print("You are not eligible!")
