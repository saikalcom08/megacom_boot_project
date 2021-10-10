# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(x):
    result = (x == 2 or x % 2 != 0)
    if result:
        for i in range(3, int(x ** 0.5), 2):
            if x % i == 0:
                return False
    return result

print(is_prime(7))