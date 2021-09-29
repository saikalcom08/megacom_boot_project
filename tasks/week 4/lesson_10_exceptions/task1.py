def summa_vektora(v1, v2):
    result = []
    for i in range(0, len(v2)):
        result.append(v1[i] + v2[i])
    return result


list1 = [11, 21, 34, 12]
list2 = [23, 25, 54, 24, 20]

try:
    print(summa_vektora(list1, list2))
except IndexError:
    print("Your vectors are differs in length")





