from creational_patterns.abstract_factory.room import Room


class RoomWithBomb(Room):

    def __init__(self):
        super().__init__()
        print('Room with Bomb\'s been created ')