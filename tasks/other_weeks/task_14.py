# Даны координаты двух точек на плоскости, требуется определить,
# лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).
# Вводятся 4 числа: координаты первой точки (x1, y1) и координаты второй точки (x2, y2).
# Вывести True или False

x1 = int(input("координаты первой точки x1: "))
y1 = int(input("координаты первой точки y2: "))
x2 = int(input("координаты второй точки x2: "))
y2 = int(input("координаты второй точки y2: "))
if x1*x2 > 0 and y1*y2 > 0:
    print(True)
else:
    print(False)