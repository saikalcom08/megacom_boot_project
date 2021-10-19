class KgToPounds:
    def __init__(self, kilogram):
        self.__kilogram = kilogram

    @property
    def to_pounds(self):
        res = round((self.__kilogram * 2.20462), 2)
        return res

    @to_pounds.setter
    def to_pounds(self, new_kg):
        self.__kilogram = new_kg

kg_to_pounds = KgToPounds(8)
#kg_to_pounds.to_pounds = 9
print(kg_to_pounds.to_pounds)
