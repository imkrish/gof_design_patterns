from abc import ABCMeta, abstractmethod


class AbstractCharacter(object, metaclass=ABCMeta):

    # Flyweight

    @abstractmethod
    def get_character(self):
        pass
