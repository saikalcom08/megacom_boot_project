# Напишите функцию sum_range(start, end), которая суммирует все целые  числа от значения «start»
# до величины «end» включительно.
# Если  пользователь задаст первое число большее чем второе, просто  поменяйте их местами.

def sum_range(start, end):
    sum = 0
    if start < end:
        for i in range(start, end+1):
            sum = sum + i
        return sum

start = int(input("start: "))
end = int(input("end: "))
try:
    result = sum_range(start, end)
except:
    k = 0
    start = k     #start = 0
    k = start     #k = 5
    start = end   #start = 4
    end = k       #end = 5
    result = sum_range(start, end)
print(result)
