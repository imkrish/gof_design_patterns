from abc import ABC
from observer import Observer


class Subject(ABC):
    
    """ Only one thing that the subject knows about its oberservers is
    they implement update method."""
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        assert isinstance(observer, Observer)
        self.__observers.append(observer)

    def detach(self, observer):
        assert isinstance(observer, Observer)
        self.__observers.remove(observer)

    def notifyAll(self):
        print('\n************************************************\nThe subject\'s notified to {} observers\n************************************************'.format(len(self.__observers)))
        """ Call update method in all of its observers """
        for observer in self.__observers:
            observer.update(self)