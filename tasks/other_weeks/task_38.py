# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

result = is_year_leap(1999)
print(result)