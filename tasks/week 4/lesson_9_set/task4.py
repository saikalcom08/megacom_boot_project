# На основании 3 исходных множеств (передаются в качестве аргументов функции diff())
# требуется написать функцию, которая будет возвращать либо симметричную разность,
# либо просто разность (если дополнительный аргумент функции symmetric имеет значение False)
# приведенных объектов в порядке: 1-ое множество, 2-ое множество, 3-е множество.


def diff(set1, set2, set3, request):
    if request == "symmetric":
        a = set1.symmetric_difference(set2).symmetric_difference(set3)
    elif request == "difference":
        a = set1.difference(set2, set3)
    return a

set1 = {2, 3, 4, 10}
set2 = {2, 5, 3}
set3 = {7, 3, 4}
request = input("Enter symmetric or difference: ")
print(diff(set1, set2, set3, request))