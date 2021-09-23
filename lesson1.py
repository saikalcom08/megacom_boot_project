# 1. Создать пустой список
# 2. Рандомно добавить в список 1000 элементов от 1 до 10
# 3. Посчитать процент четных и нечетных
# 4. Вывести максимально повторяемое число
# 5. Вывести минимально повторяемое число
# 6. Вывести число - количество повторений
import random

def my_count(numbers, number):
    counter = 0
    for i in numbers:
        if i == number:
            counter +=1
    return counter

numbers = []
evenCount = 0
oddCount = 0

total_iteration = 10

for i in range(1000):
    numbers.append(random.randint(1, total_iteration))
print("Example Numbers:", numbers)

for i in numbers:
    if (i % 2) == 0:
        evenCount += 1
    else: oddCount += 1
percentEven  = (evenCount/len(numbers)) * 100.0
percentOdd  = (oddCount/len(numbers)) * 100.0
print ("**Count of even numbers:" , evenCount, "***Count of odd numbers: ", oddCount)
print ("**Percentage of even numbers:" , percentEven,"%", "Percentage of odd numbers:", percentOdd,"%")

most_common_item = max(numbers, key = numbers.count)
print("Most common item: ", most_common_item)

least_common_item = min(numbers, key = numbers.count)
print(f ' { Least common item = : } ' )

for number in range(1, total_iteration + 1): 
    print(number, my_count(numbers, number))
