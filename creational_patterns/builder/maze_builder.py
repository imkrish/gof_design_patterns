from abc import ABCMeta, abstractmethod


class MazeBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_maze(self):
        pass

    @abstractmethod
    def build_room(self, room_number):
        pass

    @abstractmethod
    def build_door(self, room1_number, room2_number):
        pass

    @abstractmethod
    def get_maze(self):
        pass
