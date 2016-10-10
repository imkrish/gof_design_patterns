from structural_patterns.flyweight.abstract_character import AbstractCharacter


class Character(AbstractCharacter):

    # Concrete Flyweight

    def __init__(self, character):
        assert isinstance(character, str)
        assert len(character) == 1
        self.__character = character
        print(character + '\'s been created')

    def get_character(self):
        return self.__character
