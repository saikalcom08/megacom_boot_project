# Ввести стоимость телефона и количество денег в кармане.
# Вывести на экран, хватит ли денег на покупку или нет,
# если после покупки должно остаться как минимум 10 сомов на дорогу.

phone_cost = int(input("Phone costs: "))
pocket_money = int(input("How much do you have now?: "))

if phone_cost > pocket_money:
    print("You don't have enough money to buy a phone")
else:
    print("Please, buy a phone")