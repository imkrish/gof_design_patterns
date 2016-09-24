from abc import ABCMeta
from creational_patterns.abstract_factory.room import Room


class Maze(metaclass=ABCMeta):

    def __init__(self):
        self.__rooms = []
        print('Maze\'s been created created')

    def add_room(self, room):
        assert isinstance(room, Room)
        self.__rooms.append(room)