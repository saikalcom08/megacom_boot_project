# Конвертор валют

currencies = {"USD": 84.50, "RUB": 1.18, "TRY": 10.39, "EUR": 100.9}

origin = int(input("How much som do you want to change?"))
currency = (input("To which currency? (USD, RUB, TRY, EUR)")).upper()

if currency in currencies:
    res = origin * currencies[currency]
    print(res, "soms")