from abc import ABCMeta
from creational_patterns.builder.room import Room


class Maze(metaclass=ABCMeta):

    def __init__(self):
        self.__rooms = []
        print('Maze\'s been created created')

    def add_room(self, room):
        assert isinstance(room, Room)
        self.__rooms.append(room)

    def get_room(self, room_number):
        room_list = [room for room in self.__rooms if room.get_room_number() == room_number]
        if room_list:
            return room_list[0]
