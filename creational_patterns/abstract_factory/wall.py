from abc import ABCMeta


class Wall(metaclass=ABCMeta):

    def __init__(self):
        print('Wall\'s been created.')