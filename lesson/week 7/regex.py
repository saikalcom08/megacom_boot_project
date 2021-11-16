# import re
# text = "Analytics +996 555 777 666 Method AV Ptyhon Megacom examples AV +996 555 777 666"
# result = re.split(r'[+]996[ ]555[ ]\d{3}[ ]\d{3}', text)
# # print(result.group()) # works with SEARCH
# # print(result.span())
# # print(result.start())
# # print(result.end())
# print(result)

# ================================================================================

# match - will search the regular expression pattern and return the first occurrence.
# if a match is found in the first line, it returns the match object. But if a match is found in some other line,
# the Python RegEx Match function returns null.

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# ================================================================================
# search - Unlike Python re.match(), it will check all lines of the input string.
# ================================================================================
# findall - In contrast, search() module will only return the first occurrence that matches the specified pattern.
# ================================================================================

# sub - The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:
import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
# output: The9rain9in9Spain

# ================================================================================

# split() function returns a list where the string has been split at each match:
# import re
#
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# output: ['The', 'rain', 'in', 'Spain']

#=================================================================================

# compile() - впеменно сохраняет
# import re
# text = "Analytics +996 555 777 666 Method AV Ptyhon Megacom examples AV +996 555 777 666"
# result = re.split(r'[+]996[ ]555[ ]\d{3}[ ]\d{3}', text)
# pattern = re.compile("Method")
# result = pattern.findall(text)
# print(result)

# ================================================================================
# import re
# # text_demir = "6706 6205 0722 3328"
# # text_optima = "4169 5853 4609 4021"
# enter = input("Enter your card number: ")
# result_demir_master = re.findall(r'^6706[ ]\d{4}[ ]\d{4}[ ]\d{4}', enter)
# result_demir_visa = re.findall(r'', enter)
# result_optima = re.findall(r'4169[ ]5853[ ]\d{4}[ ]\d{4}', enter)
# if result_demir_master:
#     print(f'Demir Bank Master: {result_demir_master}')
# elif result_optima:
#     print(f'Optima Bank: {result_optima}')

# ==============================================================================
import re
password = input("Enter your password: ")
result = re.findall(r'(\d+\D+)([@|!|_]+)(8,32)', password)
print(result)
