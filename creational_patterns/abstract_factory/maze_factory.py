from abc import ABCMeta

from creational_patterns.abstract_factory.maze import Maze
from creational_patterns.abstract_factory.room import Room
from creational_patterns.abstract_factory.door import Door
from creational_patterns.abstract_factory.wall import Wall


class MazeFactory(metaclass=ABCMeta):

    def __init__(self):
        print('Maze Factory\'s been created.')

    def make_maze(self):
        return Maze()

    def make_room(self):
        return Room()

    def make_door(self):
        return Door()

    def make_wall(self):
        return Wall()