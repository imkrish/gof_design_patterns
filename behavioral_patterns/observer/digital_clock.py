from observer import Observer
from clock_timer import ClockTimer


class DigitalClock(Observer):

    """Concrete observer knows about concrete subject"""
    def __init__(self, subject):
        assert isinstance(subject, ClockTimer)
        subject.attach(self)
        self.__subject = subject
        
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def update(self, subject):
        self.__hour = subject.get_hour()
        self.__minute = subject.get_minute()
        self.__second = subject.get_second()
        self.__display()

    def __display(self):
        print("Digital Clock Observer => {}:{}:{}\n-------------------------------------".format(self.__hour, self.__minute, self.__second))
