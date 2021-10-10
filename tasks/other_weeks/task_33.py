# Учитывая строку, вы должны вернуть строку, в которой каждый символ (с учетом регистра) повторяется два раза.
# Пример:
# "String" ->> "SSttrriinngg"
# "Hello World" ->> "HHeelllloo WWoorrlldd"
# "1234!_ " ->> "11223344!!__ "

text = input("Enter any word: ")
for i in text:
    res = i * 2
    print(res, end="")

