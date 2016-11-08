"""
This application calculates the mean of a set of data.
It then defines the methods for you to inherit from so
you can redefine them to calculate various deviations.
The subclass for standard deviation has already been
provided.

Sample Output:

Average = 18.0
Standard Deviation = 3.03315017762062

"""

from abc import ABCMeta, abstractmethod
from math import *
DATA = [19, 15, 22, 20, 14]


class BaseDeviationCalculator(metaclass=ABCMeta):
    def __init__(self):
        self.avg = 0.0
        self.var = 0.0
        self.dev = 0.0

    def calc(self):
        self.calc_average()
        self.calc_variance()
        self.calc_deviation()

    def calc_average(self):
        """
        This method calculates the mean, but also returns it.
        This is so that the average can be calculated on the
        fly, just in case it hasn't been calculated before
        when your working out the deviation.
        """
        sum = 0
        for num in DATA:
            sum += num
        self.avg = sum / len(DATA)
        return self.avg

    @abstractmethod
    def calc_variance(self):
        pass

    @abstractmethod
    def calc_deviation(self):
        pass

    def get_average(self):
        return "Average = " + str(self.avg)

    def get_deviation(self):
        return "Deviation = " + str(self.dev)


class StdDeviationCalculator(BaseDeviationCalculator):
    def calc_variance(self):
        numerator = 0.0
        for num in DATA:
            numerator += (num - self.calc_average()) ** 2
        self.var = numerator / len(DATA)

    def calc_deviation(self):
        self.dev = sqrt(self.var)

    def get_deviation(self):
        return "Standard Deviation = " + str(self.dev)


if __name__ == "__main__":
    calc = StdDeviationCalculator()
    calc.calc()
    print(calc.get_average())
    print(calc.get_deviation())
