from creational_patterns.builder.maze_builder import MazeBuilder
from creational_patterns.builder.maze import Maze
from creational_patterns.builder.room import Room
from creational_patterns.builder.wall import Wall
from creational_patterns.builder.door import Door


class StandardMazeBuilder(MazeBuilder):

    def __init__(self):
        self.__maze = None  # this object is kept track

    def build_maze(self):
        self.__maze = Maze()

    def build_room(self, room_number):
        assert isinstance(room_number, int)
        if not self.__maze.get_room(room_number):
            room = Room(room_number)
            self.__maze.add_room(room)

            room.set_side(Room.NORTH, Wall())
            room.set_side(Room.SOUTH, Wall())
            room.set_side(Room.EAST, Wall())
            room.set_side(Room.WEST, Wall())

    def build_door(self, room1_number, room2_number):
        room1 = self.__maze.get_room(room1_number)
        room2 = self.__maze.get_room(room2_number)
        if room1 and room2:
            door = Door(room1, room2)
            room1.set_side(self.__common_wall(room1, room2), door)
            room2.set_side(self.__common_wall(room2, room1), door)

    def get_maze(self):
        return self.__maze

    def __common_wall(self, room1, room2):
        room1_number = room1.get_room_number()
        room2_number = room2.get_room_number()

        if room1_number - room2_number == 1:
            return Room.WEST
        elif room1_number - room2_number == -1:
            return Room.EAST
        else:
            raise ValueError('These 2 rooms are not next to each other')
