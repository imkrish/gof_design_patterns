from abc import ABC
from behavioral_patterns.observer.observer import Observer


class Subject(ABC):

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        assert isinstance(observer, Observer)
        self.__observers.append(observer)

    def detach(self, observer):
        assert isinstance(object, Observer)
        self.__observers.remove(observer)

    def notifyAll(self):
        for observer in self.__observers:
            observer.update(self)