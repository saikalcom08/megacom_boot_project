# Задача:
# Если задано целое число, например 3, возвращается строка:  "1 sheep...2 sheep...3 sheep..."
# Если задано целое число, например 2, возвращается строка:  "1 sheep...2 sheep..."
# Если задано целое число, например 4, возвращается строка:  "1 sheep...2 sheep...3 sheep...4 sheep..."

number = int(input("Введите любое число: "))
for i in range(1, number+1):
    print(i, "sheep")