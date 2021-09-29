# EXCEPTIONS

# k = 10/0
# print(k)

# try:
#     k = 10/0
# except ZeroDivisionError:
#     k = 0
# print(k)

# try:
#     k = 10 / 0
# except: print("sorry, you can't delete a number to 0")
#========================================================

# lists = []
#
# for i in range(5):
#     a = input("Enter number:")
#     lists.append(a)
# print(lists)
# try:
#     average = sum(lists)/len(lists)
# except TypeError:
#     average = 0
# print(average)
#==========================================================
# def integer_maker(lists):
#     result = []
#     for i in lists:
#         result = lists.append(int(i))
#     return result
#
# lists = []
# for i in range(5):
#     a = input("Enter number:")
#     lists.append(a)
# try:
#     average = sum(lists)/len(lists)
# except TypeError:
#     a = integer_maker(lists)
#     average = sum(a) / len(a)
#
# print(average)
#=================================================
# try:
#     k = 10/0
# except ZeroDivisionError:
#     raise Exception("You can't divide to 0")
#===================================================
# file = open('test_new.txt', 'w')
# list1 = [x for x in range(1, 1001) if x%2 == 0]
# list2 = [x for x in range(1, 1001) if x%5 == 0 and x%6 == 0]
# file.write(str(list1) + "\n\n" + str(list2))
#file.close()
#===================================================
# TASK #4
# def diff(set1, set2, set3, request):
#     if request == "symmetric":
#         a = set1.symmetric_difference(set2).symmetric_difference(set3)
#     elif request == "difference":
#         a = set1.difference(set2, set3)
#     return a
#
# set1 = {2, 3, 4, 10}
# set2 = {2, 5, 3}
# set3 = {7, 3, 4}
# request = input("Enter symmetric or difference: ")
# print(diff(set1, set2, set3, request))

