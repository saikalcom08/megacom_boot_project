class Student:
    def __init__(self, name="Ivan", groupNumber="10A", age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
        return self.name, self.age
    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber
        return self.groupNumber

student1 = Student("Saikal", "1D", 31)
student2 = Student("Eldar", "2D", 22)
student3 = Student("Viktoriya", "10S", 20)
student4 = Student("Meerim", "6F", 18)
student5 = Student("Kyal", "9V", 19)

print(student1.getName())
print(student2.getAge())
print(student3.getGroupNumber())
print(student4.setNameAge(student4.name, student4.age))
print(student5.setGroupNumber("8A"))