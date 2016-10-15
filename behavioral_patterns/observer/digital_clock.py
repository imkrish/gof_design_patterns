from behavioral_patterns.observer.observer import Observer


class DigitalClock(Observer):

    def __init__(self, subject):
        super().__init__(subject)
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def update(self, subject):
        self.__hour = subject.get_hour()
        self.__minute = subject.get_minute()
        self.__second = subject.get_second()
        self.__draw()

    def __draw(self):
        print("Digital Clock => {}:{}:{}".format(self.__hour, self.__minute, self.__second))
