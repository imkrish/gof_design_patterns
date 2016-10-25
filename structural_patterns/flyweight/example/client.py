from structural_patterns.flyweight.character_factory import CharacterFactory


if __name__ == '__main__':

    character_factory = CharacterFactory()
    character_factory.get_character('a')
    character_factory.get_character('c')
    character_factory.get_character('a')
    character_factory.get_character('z')
    character_factory.get_character('d')
    character_factory.get_character('z')
    character_factory.get_character('c')
    character_factory.get_character('e')
    character_factory.get_character('a')
    character_factory.get_character('e')

    print(character_factory.get_num_created_character())