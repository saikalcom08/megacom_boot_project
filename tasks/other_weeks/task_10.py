# Создать переменную для хранения желаемой марки автомобиля.
# В консоли ввести название и проверить, введена желаемая или нет. Вывести True или False

desired_car = "jeep"
find_car = input("enter a name of desired car: ").lower()
if desired_car == find_car:
    print(True)
else:
    print(False)