from abc import ABC, abstractmethod


class MonsterFactory(object):

    """ConcreteFlyweightFactory"""

    def __init__(self):
        self.__monsters = {}

        Orc("Orc")

    def get_monster(self, monster_type):
        if monster_type not in self.__monsters:
            new_monster = eval(monster_type + '("' + monster_type + '")')
            # Check whether this object is an instance of Monster.
            assert isinstance(new_monster, Monster)
            # Then assign to a monster pool.
            self.__monsters[monster_type] = new_monster

        return self.__monsters[monster_type]


class Monster(ABC):

    """Flyweight"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def draw(self, x, y, z):
        """ Default Implementation """
        print('A {} is drawn at {}, {}, {}.'.format(self._name, x, y, z))


class Orc(Monster):

    """Concrete Flyweight"""

    # def __init__(self):
    #     super().__init__('Orc')

    def draw(self, x, y, z):
        # Use default implementation from parent class
        super().draw(x, y, z)


class Goblin(Monster):

    """Concrete Flyweight"""

    # def __init__(self):
    #     super().__init__('Golbin')

    def draw(self, x, y, z):
        # Use default implementation from parent class
        super().draw(x, y, z)


def client():

    """Client uses FlyweightFactory object to get the ConcreteFlyweight objects from the pool"""

    monster_factory = MonsterFactory()
    monster1 = monster_factory.get_monster('Orc')
    monster1.draw(1, 3, 5)

    monster2 = monster_factory.get_monster('Orc')
    monster2.draw(2, 5, 1)

    monster3 = monster_factory.get_monster('Orc')
    monster3.draw(3, 4, 6)

    monster4 = monster_factory.get_monster('Goblin')
    monster4.draw(1, 1, 7)

    monster5 = monster_factory.get_monster('Goblin')
    monster5.draw(1, 3, 4)

    monster6 = monster_factory.get_monster('Goblin')
    monster6.draw(3, 4, 6)


if __name__ == '__main__':
    client()

