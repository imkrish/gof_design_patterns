from creational_patterns.abstract_factory.room import Room
from creational_patterns.abstract_factory.maze_factory import MazeFactory
from creational_patterns.abstract_factory.bombed_maze_factory import BombedMazeFactory


def create_maze(maze_factory):
    assert isinstance(maze_factory, MazeFactory)
    maze = maze_factory.make_maze()
    room1 = maze_factory.make_room()
    room2 = maze_factory.make_room()
    door = maze_factory.make_door()

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Room.NORTH, maze_factory.make_wall())
    room1.set_side(Room.EAST, door)
    room1.set_side(Room.SOUTH, maze_factory.make_wall())
    room1.set_side(Room.WEST, maze_factory.make_wall())

    room2.set_side(Room.NORTH, maze_factory.make_wall())
    room2.set_side(Room.EAST, maze_factory.make_wall())
    room2.set_side(Room.SOUTH, maze_factory.make_wall())
    room2.set_side(Room.WEST, door)


if __name__ == '__main__':
    normal_maze_factory = MazeFactory()
    create_maze(normal_maze_factory)
    print('-------------------------------------')
    bombed_maze_factory = BombedMazeFactory()
    create_maze(bombed_maze_factory)