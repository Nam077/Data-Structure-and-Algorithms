def position_character(character):
    return ord(character)


if __name__ == '__main__':
    print("Enter character: ")
    character_input = input()
    print("Position =", position_character(character_input))
