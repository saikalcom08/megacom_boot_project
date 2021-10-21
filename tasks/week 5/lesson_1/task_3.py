class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")
    def stop(self):
        print("Автомобиль заглушен")
    def set_year(self, year):
        self.year = year
        return self.year
    def set_type(self, type):
        self.type = type
        return self.type
    def set_color(self, color):
        self.color = color
        return self.color

car1 = Car("yellow", "Mers", 2000)
car1.start()
car1.stop()
print(car1.set_year(1998))
print(car1.set_type("Jeep"))
print(car1.set_color("black"))