from subject import Subject
from interval import Interval
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
        """ 
        This subject will change its states(hour, minute, second) every 3 seconds, 
        and then notify all of its observers
        """
        def set_current_time():
            now = datetime.datetime.now()
            self.__hour = now.hour
            self.__minute = now.minute
            self.__second = now.second
            self.notifyAll()

        self.__interval = Interval(set_current_time, 3)

    def cancel_interval(self):
        self.__interval.cancel()

    
    def get_hour(self):
        """
        For observers to get this state
        """
        return self.__hour

    def get_minute(self):
        """
        For observers to get this state
        """
        return self.__minute

    def get_second(self):
        """
        For observers to get this state
        """
        return self.__second