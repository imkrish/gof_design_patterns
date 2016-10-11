import abc
from enum import Enum


# Enum to eliminate string literals.
class BMWCarType(Enum):
    bmw_z4 = 0
    bmw_series_3 = 1


# Creator
class CarFactory(abc.ABC):

    @abc.abstractmethod
    def build_car(self, model):
        """ Check the model, build a car, and return it."""

    def get_car_model(self, model):
        car = self.build_car(model)
        assert isinstance(car, Car)
        return car.get_model()


# ConcreteCreator
class BMWFactory(CarFactory):

    def build_car(self, model):
        if model == BMWCarType.bmw_z4:
            return BMWZ4()
        elif model == BMWCarType.bmw_series_3:
            return BMWSeries3()
        else:
            raise ValueError('Cannot build this car model: ' + str(model))


# Product
class Car(abc.ABC):

    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model


# Concrete Product A
class BMWZ4(Car):

    def __init__(self):
        super().__init__('BMW Z4')


# Concrete Product B
class BMWSeries3(Car):

    def __init__(self):
        super().__init__('BMW Series 3')


if __name__ == '__main__':

    bmw_factory = BMWFactory()
    print(bmw_factory.get_car_model(BMWCarType.bmw_series_3))
    print(bmw_factory.get_car_model(BMWCarType.bmw_z4))