from creational_patterns.builder.maze_builder import MazeBuilder


class MazeDirector(object):

    def __init__(self, maze_builder):
        assert isinstance(maze_builder, MazeBuilder)
        self.__maze_builder = maze_builder

    def create_maze(self):
        self.__maze_builder.build_maze()
        self.__maze_builder.build_room(1)
        self.__maze_builder.build_room(2)
        self.__maze_builder.build_door(1, 2)
