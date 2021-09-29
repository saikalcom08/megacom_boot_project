# FILES
# file = open("test.txt")
# a = file.read()
# a = file.readline()
# file.close()
# print(a)

#============================
# file = open("test.txt", "w")
# file.write("morning python bootcamp")
# file.close()
#
# file2 = open("test_1.txt", "w") #esli ne naidet test.txt , to otkroet test_1.txt
# file2.write("morning 2 python bootcamp")
# file2.close()

#=============================
# file = open('test.txt', 'a')
# file.write(" Privet")
# file.close()

#=============================
# file = open('test.txt', 'a+')
# file.write(" Privet")
# a = file.read()
# print(a)
#==============================
# file = open("test.txt", "rb")
# a = file.read()
# print(a)

#==============================
# file = open('test_new.txt', 'w')
# list1 = [x for x in range(1, 1001) if x%2 == 0]
# list2 = [x for x in range(1, 1001) if x%5 == 0 and x%6 == 0]
# file.write(str(list1) + "\n\n" + str(list2))
# file.close()

#==============================
# from lesson10 import file
# file.write("\nadding some lines")
#==============================
# with open("numbers.txt", "w") as file:
#     file.write("Hello")
# #file.write('bye')
#==============================
# file = open("numbers.txt", 'r')
# a = file.readlines(2)
# print(a)
#==============================
file = open("numbers.txt", 'a')
file.seek(2)
file.write("\nI am one")
