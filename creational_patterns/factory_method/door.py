from abc import ABCMeta
from creational_patterns.factory_method.room import Room


class Door(metaclass=ABCMeta):
    def __init__(self, room1, room2):
        assert isinstance(room1, Room) and isinstance(room2, Room)
        self.__room1 = room1
        self.__room2 = room2
        print('Door\'s been created.')