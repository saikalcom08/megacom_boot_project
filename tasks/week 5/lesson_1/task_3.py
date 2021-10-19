class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")
    def stop(self):
        print("Автомобиль заглушен")
    def get_year(self):
        return self.year
    def get_type(self):
        return self.type
    def get_color(self):
        return self.color

car1 = Car("yellow", "Mers", 2000)
car1.start()
car1.stop()
print(car1.get_year())
print(car1.get_type())
print(car1.get_color())