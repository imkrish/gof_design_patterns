from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        """ Implement update method for concrete observer """




