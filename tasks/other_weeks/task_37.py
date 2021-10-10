# Написать функцию month_to_season(month_number),
# которая принимает  аргумент - month_number - и возвращает название сезона, к которому относится этот месяц.

def month_to_season(month_number):
    if 3 <= month_number <= 5:
       return "Spring"
    elif 6 <= month_number <= 8:
        return "Summer"
    elif 9 <= month_number <= 11:
        return "Autumn"
    elif month_number in [1, 2, 12]:
        return "Winter"
    else:
        return "There is no such month."
    return month_number

result = month_to_season(12)
print(result)