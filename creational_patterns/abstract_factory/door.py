from abc import ABCMeta


class Door(metaclass=ABCMeta):
    def __init__(self):
        print('Door\'s been created.')