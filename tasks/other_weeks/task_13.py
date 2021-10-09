# Выбор дома будет осуществляться по району, стоимостью, строительных материалов и состоянию, размером участка.
#
# Дом нужен в районе чон арык, байтик или ортосай
# Если дом из кирпича и участок до 4 соток, то стоимость должна быть не более 50000.
# Если дом из пескоблока и участок до 5 соток, то стоимость должна быть не более 45000.

region = input("Region: ").lower()
cost = int(input("Cost: "))
material = input("Building materials: ").lower()
area = int(input("Area: "))

if region in ["chon aryk", "baitik", "orto sai"] and ((material == "brick" or area >= 4 or cost <= 50000) or
                                                    (material == "sand block" or area >= 5 or cost <= 45000)):
    print("Will buy!")
else:
    print("Will not buy!")