# class BMW:
#     def __init__(self, model, color, volume):
#         self.model = model
#         self.color = color
#         self.volume = volume
#         #super(BMW, self).__init__(model, color, volume)
#
# class Toyota:
#     def __init__(self, engine, wheels):
#         self.engine = engine
#         self.wheels = wheels
#         #super(Toyota, self).__init__(engine, wheels)
#
# class BMWToyota(Toyota, BMW):
#     def __init__(self, model, volume, color, engine, wheels, seat_place):
#         super().__init__(model, volume, color)
#         super(Toyota, self).__init__(engine, wheels)
#         #BMW.__init__(self, model, volume, color)
#         #Toyota.__init__(self, engine, wheels)
#         self.seat_place = seat_place
#         super().__init__()
#
#     def create(self):
#         print(f"car model - {self.model}, color - {self.color}, \
#               engine - {self.engine}, volume - {self.volume}, wheels - {self.wheels}, \
#               seat place - {self.seat_place}")
#
# car = BMWToyota("Camry", "3.3", "black", "3234", 4, 7)
# car.create()

# =========================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiple(self):
        return self.x * self.y

    def prin(self):
        print("Hello World")

class A:
    def prin(self):
        print("Hello")

class Parabola(Point, A):
    def __init__(self, x, y, c):
        #Point.__init__(self, x, y)
        super().__init__(x, y)
        self.c = c

    def prin(self):
        #return super().multiple() * self.c
        return super().prin()

parabola1 = Parabola(2, 4, 6)
print(parabola1.prin())