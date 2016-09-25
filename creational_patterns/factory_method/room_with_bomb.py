from creational_patterns.factory_method.room import Room


class RoomWithBomb(Room):

    def __init__(self, room_number):
        super().__init__(room_number)
        print('Room with bomb\'s been created.')