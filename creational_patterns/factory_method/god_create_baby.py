import abc


# Product
class Mind(abc.ABC):
    pass


# Concrete Product
class GoodAttitude(Mind):

    def __str__(self):
        return 'Sugar & Spice.'


# Concrete Product
class GoodTemperament(Mind):

    def __str__(self):
        return 'All things nice!'


# Creator
class Baby(abc.ABC):

    def __init__(self):
        self._personality = []
        self._age = 0
        self._value = 'Baby'
        # call factory method, when creating this object
        self._create_minds()

    @abc.abstractmethod
    def _create_minds(self):
        # Factory Method
        """ Depend on the kind of baby, add personalities and set the value"""

    def __str__(self):
        me = "\nI am made up of..."
        for thing in self._personality:
            me += "\n" + str(thing)
        me += "\nMy age is " + str(self._age)
        me += "\nI am " + self._value
        return me


# Concrete Creator
class GoodBaby(Baby):

    # Factory Method
    def _create_minds(self):
        self._personality.append(GoodAttitude())
        self._personality.append(GoodTemperament())
        self._value = "treasured!"


# Concrete Creator
class ChallengingBaby(Baby):

    # Factory Method
    def _create_minds(self):
        self._personality.append(GoodTemperament())
        self._personality.append(GoodAttitude())
        self._value = "happy!"


if __name__ == "__main__":
    girl = GoodBaby()
    print(girl)
    boy = ChallengingBaby()
    print(boy)