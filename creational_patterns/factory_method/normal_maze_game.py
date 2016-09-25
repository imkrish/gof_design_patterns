from creational_patterns.factory_method.maze_game import MazeGame
from creational_patterns.factory_method.maze import Maze
from creational_patterns.factory_method.room import Room
from creational_patterns.factory_method.door import Door
from creational_patterns.factory_method.wall import Wall


class NormalMazeGame(MazeGame):

    def make_door(self, room1, room2):
        assert isinstance(room1, Room) and isinstance(room2, Room)
        return Door(room1, room2)

    def make_wall(self):
        return Wall()

    def make_maze(self):
        return Maze()

    def make_room(self, room_number):
        return Room(room_number)


if __name__ == '__main__':
    normal_maze_game = NormalMazeGame()
    normal_maze_game.create_maze()