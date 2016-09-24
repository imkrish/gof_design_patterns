from creational_patterns.abstract_factory.wall import Wall


class BombedWall(Wall):

    def __init__(self):
        print('Bombed wall\'s been created ')