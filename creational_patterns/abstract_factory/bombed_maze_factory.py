from creational_patterns.abstract_factory.maze_factory import MazeFactory
from creational_patterns.abstract_factory.bombed_wall import BombedWall
from creational_patterns.abstract_factory.room_with_bomb import RoomWithBomb


class BombedMazeFactory(MazeFactory):

    def __init__(self):
        # super(BombedMazeFactory, self).__init__()
        super().__init__()
        print('Bombed Mazed Factory\'s been created')

    def make_room(self):
        return RoomWithBomb()

    def make_wall(self):
        return BombedWall()
