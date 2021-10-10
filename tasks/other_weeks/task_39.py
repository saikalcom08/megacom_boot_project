# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения:
# периметр квадрата, площадь квадрата и диагональ квадрата.

import math
def square(a):
    d_kv = math.sqrt(2) * a
    p_kv = 4 * a
    a_kv = a ** 2
    return p_kv, a_kv, d_kv

result = square(7)
print(result)