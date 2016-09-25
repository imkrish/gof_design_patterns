from abc import ABCMeta


class Room(metaclass=ABCMeta):

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 4

    def __init__(self, number):
        self.__sides = {}
        self.__room_number = number
        print('Room\'s been created.')

    def get_room_number(self):
        return self.__room_number

    def set_side(self, side, wall_or_door):
        from creational_patterns.factory_method.door import Door
        from creational_patterns.factory_method.wall import Wall
        assert isinstance(wall_or_door, Wall) or isinstance(wall_or_door, Door)
        if side == Room.NORTH:
            self.__sides[Room.NORTH] = wall_or_door
        elif side == Room.EAST:
            self.__sides[Room.EAST] = wall_or_door
        elif side == Room.SOUTH:
            self.__sides[Room.SOUTH] = wall_or_door
        elif side == Room.WEST:
            self.__sides[Room.WEST] = wall_or_door
        else:
            raise ValueError('Value for side is invalid.')