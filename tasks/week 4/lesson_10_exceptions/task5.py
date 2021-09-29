# Создайте функцию которое делает простое шифрование принимает 2  аргумента
# 1)данные которые нужно зашифровать 2) ключ сдвига
# На выходе должно получится зашифрованное сообщение
# но вначале строки  нужно добавить рандомное число и в конце тоже дорлжно быть рандомное  число от 0 до 1
# Например : если на вход приходнят данные (“Hello world”, 3) На выходе получает “2lo worldhell0.111”

import random

def enryption(word, key_space):
    beginning = random.randint(0, 9)
    middle = word[::-1]
    ending = round(random.random(), 2)
    the_word = str(beginning) + middle + str(ending)
    a = the_word.replace(" ", "")
    result = a[:int(key_space)] + " " + a[int(key_space):]
    return result


example_word = input("Enter your word: ")
shift_key = input("Enter shift key: ")
print(enryption(example_word, shift_key))