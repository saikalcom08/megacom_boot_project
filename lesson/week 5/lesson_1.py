class Person():
    eyes = 2
    nose = 1
    ears = 2

    def run(self):
        print("person running")

    def get_info(self):
        print(f'У этого человека есть {self.eyes} глаза, {self.nose} нос, {self.ears} уха')
        # return get_i

person_1 = Person()
person_2 = Person()
person_3 = Person()
person_1.get_info()
# person_1.eyes = 4
# print(person_1.eyes, "eyes")
# print(person_1.eyes, "noses")
# person_2 = Person()
# person_2.nose = 3
# print(person_2.eyes, "eyes")
# # print(person_1.ears)
# # print(person_1.nose)
# # print(person_1.eyes)