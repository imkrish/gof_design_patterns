from creational_patterns.builder.maze_director import MazeDirector
from creational_patterns.builder.standard_maze_builder import StandardMazeBuilder


if __name__ == '__main__':

    builder = StandardMazeBuilder()
    director = MazeDirector(builder)
    director.create_maze()
    print(builder.get_maze())