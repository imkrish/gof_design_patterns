from abc import ABCMeta, abstractmethod
from creational_patterns.factory_method.room import Room


class MazeGame(metaclass=ABCMeta):

    def create_maze(self):
        maze = self.make_maze()
        room1 = self.make_room(1)
        room2 = self.make_room(2)
        door = self.make_door(room1, room2)

        maze.add_room(room1)
        maze.add_room(room2)

        room1.set_side(Room.NORTH, self.make_wall())
        room1.set_side(Room.EAST, door)
        room1.set_side(Room.SOUTH, self.make_wall())
        room1.set_side(Room.WEST, self.make_wall())

        room2.set_side(Room.NORTH, self.make_wall())
        room2.set_side(Room.EAST, self.make_wall())
        room2.set_side(Room.SOUTH, self.make_wall())
        room2.set_side(Room.WEST, door)

    # Factory methods
    @abstractmethod
    def make_maze(self):
        pass

    @abstractmethod
    def make_room(self, room_number):
        pass

    @abstractmethod
    def make_door(self, room1, room2):
        pass

    @abstractmethod
    def make_wall(self):
        pass