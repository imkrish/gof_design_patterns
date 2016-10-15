from abc import ABC, abstractmethod


class Observer(ABC):

    def __init__(self, subject):
        from behavioral_patterns.observer.subject import Subject
        assert isinstance(subject, Subject)
        self.__subject = subject
        self.__subject.attach(self)

    @abstractmethod
    def update(self, subject):
        """ Implement update for concrete observer """
