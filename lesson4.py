# tuple
# mutable and immutable variables
#=====================================

# def get_cash(cash_list, expense):
#     count = 0
#     for i in cash_list:
#         count += i
#     profit = count - (count * expense)
#     return profit
#
# cash = [7854, 3458, 9582, 234,  3490, 20348, 34985]
# expense = 0.2
# print(get_cash(cash, expense))
#=========================================================
#args - sends a list of values to a function, kwargs - sends a dictionary with values associated with keywords to a function
# def get(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get(1, 'A', True, a=10, b=False)
#====================================================
# def kpi(**kwargs):
#     count = len(kwargs)
#     shet = 0
#     for x in kwargs.values():
#         shet += x
#     return shet/count
#
#     # print(kwargs)
#     # print(kwargs['mat']) #programma slomaetsia
#     # print(kwargs.get('fiz', None)) # luchshe ispol'zovat' get
#
# print(kpi(mat=100, him=90))

#========================================================
# dict1 = {"k":1, "h":4, "bool" : True}
# for x, y in dict1.items():
#     print(x,y)
#==========================================================
# def get_num(*args):
#     return sum(args)
#
# print(get_num(1, 2, 3, 4, 5, 6))
#=======================================================
def get_num(*args):
    a = 0
    for i in args:
        if type(i) == int:
            a += i
    return a

print(get_num(1, False, 2, 3, 4, 'True', 5, 6, ['a', 'v']))
#======================================================

