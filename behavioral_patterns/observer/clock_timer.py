from behavioral_patterns.observer.subject import Subject
from behavioral_patterns.observer.interval import Interval
import datetime


class ClockTimer(Subject):

    def __init__(self):
        super().__init__()
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
        self.__interval = 0
        self.__tick()

    def __tick(self):

        def set_current_time():
            now = datetime.datetime.now()
            self.__hour = now.hour
            self.__minute = now.minute
            self.__second = now.second
            self.notifyAll()

        self.__interval = Interval(set_current_time, 1)

    def cancel_interval(self):
        assert isinstance(self.__interval, Interval)
        self.__interval.cancel()

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second