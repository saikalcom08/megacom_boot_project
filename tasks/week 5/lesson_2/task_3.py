class Tomato:
    states = {"Отсутствует", "Цветение", "Зеленый", "Красный"}
    def __init__(self, index):

        self._index = index
        self._state = 0

    def grow(self):
        pass

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    @staticmethod
    def knowledge_base():
        print('''Early-season tomatoes require 50 to 60 days to reach 
        harvest from transplanting; mid-season tomatoes require 60 to 80 days; 
        late-season tomatoes require 80 or more days. 
        In hot summer-mild winter regions such as USDA zone 10 or warmer, 
        tomatoes can be grown as a fall and winter crop.''')
Gardener.knowledge_base()
tomato_bush = TomatoBush(5)
gardener = Gardener("Saikal", tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

