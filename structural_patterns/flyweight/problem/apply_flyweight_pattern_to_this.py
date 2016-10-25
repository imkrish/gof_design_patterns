# -----------------------------------------------------------------------------
# Name:        Flyweight/beforeFlyweight
# Purpose:     
#
# Author:      xul
#
# Created:     10:20 AM 29/05/15
# Copyright:   (c) xul 10:20 AM 29/05/15
# Licence:     <your licence>
# -----------------------------------------------------------------------------


class Aircraft(object):
    def __init__(self, asset_number, bought_date, wingspan, capacity, speed,
                 range):
        self.asset_number = asset_number
        self.bought_date = bought_date
        self.wingspan = wingspan
        self.capacity = capacity
        self.speed = speed
        self.range = range

    def get_details(self):
        return "Asset Number: %d\nCapacity: %d people\nWingspan: %d m\nSpeed: %d km/h\nRange: %d km\nBought: %s" % (
            self.asset_number, self.capacity, self.wingspan, self.speed,
            self.range,
            self.bought_date)


class Boeing797(Aircraft):
    def __init__(self, asset_number, bought_date):
        super().__init__(asset_number, bought_date, 80.8, 1000, 1046, 14400)


class Airbus380(Aircraft):
    def __init__(self, asset_number, bought_date):
        super().__init__(asset_number, bought_date, 79.8, 555, 912, 10370)


if __name__ == '__main__':
    fleet = [Airbus380(1001, '10-May-2007'),
             Airbus380(1002, '10-Nov-2007'),
             Boeing797(1003, '10-May-2008'),
             Boeing797(1004, '10-Nov-2008')]

    [print(aircraft, '\n', aircraft.get_details(), '\n') for aircraft in fleet]
