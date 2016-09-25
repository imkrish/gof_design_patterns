from creational_patterns.factory_method.maze_game import MazeGame
from creational_patterns.factory_method.maze import Maze
from creational_patterns.factory_method.room_with_bomb import RoomWithBomb
from creational_patterns.factory_method.door import Door
from creational_patterns.factory_method.bombed_wall import BombedWall


class BombedMazeGame(MazeGame):

    def make_door(self, room1, room2):
        assert isinstance(room1, RoomWithBomb) and isinstance(room2, RoomWithBomb)
        return Door(room1, room2)

    def make_wall(self):
        return BombedWall()

    def make_maze(self):
        return Maze()

    def make_room(self, room_number):
        assert isinstance(room_number, int)
        return RoomWithBomb(room_number)

if __name__ == '__main__':

    bombed_maze_game = BombedMazeGame()
    bombed_maze_game.create_maze()