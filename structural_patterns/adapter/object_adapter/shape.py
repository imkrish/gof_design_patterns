from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def bounding_box(self, bottom_left, top_right):
        pass

    @abstractmethod
    def create_manipulator(self):
        pass
