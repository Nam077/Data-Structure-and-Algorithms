def character_in_string(string):
    return list(string)


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    print("Characters =", character_in_string(string_input))
