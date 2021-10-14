class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return f"{self.a} + {self.b} = {self.a+self.b}"

    def multiplication(self):
        return f"{self.a} * {self.b} = {self.a*self.b}"

    def division(self):
        return f"{self.a} / {self.b} = {round((self.a/self.b),1)}"

    def substraction(self):
        return f"{self.a} - {self.b} = {self.a-self.b}"

math1 = Math(786, 83)
print(math1.addition())
print(math1.multiplication())
print(math1.division())
print(math1.substraction())

math2 = Math(45, 21)
print(math2.addition())
print(math2.multiplication())
print(math2.division())
print(math2.substraction())