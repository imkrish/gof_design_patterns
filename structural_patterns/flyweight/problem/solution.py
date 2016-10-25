from abc import ABC, abstractmethod


class AircraftFactory(object):

    def __init__(self):
        self.__aircraft = {}

    def get_aircraft(self, aircraft_type):
        if aircraft_type not in self.__aircraft:
            self.__aircraft[aircraft_type] = eval(aircraft_type + '()')
        return self.__aircraft[aircraft_type]


class Aircraft(ABC):

    def __init__(self, wingspan, capacity, speed, range):
        self.__wingspan = wingspan
        self.__capacity = capacity
        self.__speed = speed
        self.__range = range

    @abstractmethod
    def get_details(self, asset_number, bought_date):
        return 'Asset Number: {}\nCapacity: {}\nWingspan: {}\nSpeed: {} km/h\nRange: {} km\nBought: {}'\
                .format(asset_number, self.__capacity, self.__wingspan, self.__speed, self.__range, bought_date)


class Boeing797(Aircraft):

    def __init__(self):
        super().__init__(80.8, 1000, 1046, 14400)

    def get_details(self, asset_number, bought_date):
        return super().get_details(asset_number, bought_date)


class Airbus380(Aircraft):

    def __init__(self):
        super().__init__(79.8, 555, 912, 10370)

    def get_details(self, asset_number, bought_date):
        return super().get_details(asset_number, bought_date)


def client():

    aircraft_factory = AircraftFactory()

    aircraft = aircraft_factory.get_aircraft('Airbus380')
    print(id(aircraft))
    print(aircraft.get_details(1001, '10-May-2007') + '\n')

    aircraft = aircraft_factory.get_aircraft('Airbus380')
    print(id(aircraft))
    print(aircraft.get_details(1002, '10-Nov-2007') + '\n')

    aircraft = aircraft_factory.get_aircraft('Boeing797')
    print(id(aircraft))
    print(aircraft.get_details(1003, '10-May-2008') + '\n')

    aircraft = aircraft_factory.get_aircraft('Boeing797')
    print(id(aircraft))
    print(aircraft.get_details(1004, '10-Nov-2008') + '\n')


if __name__ == '__main__':
    client()
