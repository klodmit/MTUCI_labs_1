# Создать класс человек и создать в нем метод «рождение»
# где пол ребенка выбирается 50 на 50. Создать 2 дочерних класса мальчик и девочка.
# Метод «рождение» должен создавать объекты мальчик и девочка.
# Написать программу, которая выясняет пол ребенка и дает ему соответствующее имя.
# Мальчик не должен мочь рожать.
import random


class Human():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def Born(self):
        if random.random() > 0.5:
            child = Boy()
        else:
            child = Girl()
        return child


class Boy(Human):
    def __init__(self):
        self.age = 0

    def Born(self):
        print('не получается')


class Girl(Human):
    def __init__(self):
        self.age = 0


parent = Human(24, 'Мама')
child_1 = parent.Born()
print(type(child_1))
child_1.name = 'Саша'
print(child_1.name)
parent1 = Boy()
parent1.Born()
parent2 = Girl()
child2 = parent2.Born()
if 'Boy' in str(type(child2)):
    child2.name = 'Олег'
else:
    child2.name = 'Оля'
print(child2.name)
print(type(child2))
