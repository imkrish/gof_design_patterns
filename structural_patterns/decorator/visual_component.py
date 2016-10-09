from abc import ABCMeta, abstractmethod


class VisualComponent(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass
