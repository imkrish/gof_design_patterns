from abc import ABC
from behavioral_patterns.observer.observer import Observer


class Subject(ABC):

    def __init__(self):
        self.__list = []

    def attach(self, observer):
        assert isinstance(observer, Observer)
        self.__list.append(observer)

    def detach(self, observer):
        assert isinstance(object, Observer)
        self.__list.remove(observer)

    def notifyAll(self):
        for observer in self.__list:
            observer.update(self)