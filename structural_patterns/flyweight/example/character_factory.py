from structural_patterns.flyweight.character import Character


class CharacterFactory(object):

    # Flyweight Factory

    def __init__(self):
        self.__list = {}

    def get_character(self, char):
        if char not in self.__list:
            self.__list[char] = Character(char)
        return self.__list[char]

    def get_num_created_character(self):
        return len(self.__list)