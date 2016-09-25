from creational_patterns.factory_method.wall import Wall


class BombedWall(Wall):

    def __init__(self):
        super().__init__()
        print('Bombed wall\'s been created')