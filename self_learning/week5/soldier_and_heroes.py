from random import randint, choice

class Human:
    def __init__(self, uid, team, name):
        self.uid = uid
        self.team = team
        self.name = name

class Soldier(Human):
    def __init__(self, uid, team, name):
        super().__init__(uid, team, name)

    def follow_hero(self):
        print(f"Follow HEro")

class Hero(Human):
    def __init__(self, uid, team, name):
        super().__init__(uid, team, name)
        self.__level = 0

    def level_up(self):
        self.__level += 1

    def get_level(self):
        return self.__level

class Team:
    def __init__(self, name):
        self.name = name
        self.team_members = []

    def add_hero(self, hero):
        self.hero = hero

    def add_member(self, soldier):
        self.team_members.append(soldier)

    def count_members(self):
        return len(self.team_members)

# Teams
team1 = Team("white")
team2 = Team("black")

teams = [team1, team2]

# Heroes
hero1 = Hero(1, team1, "Hero1")
team1.add_hero(hero1)

hero2 = Hero(2, team2, "Hero2")
team2.add_hero(hero2)

# Program starts
n = int(input("Number of soldiers: "))

for i in range(n):
    team_index = randint(0, 1)
    soldier = Soldier(i, teams[team_index], f"Soldier {i}")
    teams[team_index].add_member(soldier)

print(f"Team 1: {team1.count_members()}")
print(f"Team 2: {team2.count_members()}")
print()

if team1.count_members() > team2.count_members():
    team1.hero.level_up()
elif team1.count_members() == team2.count_members():
    team1.hero.level_up()
    team2.hero.level_up()
else:
    team2.hero.level_up()

print(f"Level of {hero1.name}: {hero1.get_level()}")
print(f"Level of {hero2.name}: {hero2.get_level()}")
print()

soldier = choice(hero1.team.team_members)
soldier.follow_hero()
print(f"ID of hero ({hero1.name}): {hero1.uid} ")
print(f"ID of soldier ({soldier.name}): {soldier.uid}")
