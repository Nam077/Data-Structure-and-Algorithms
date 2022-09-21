def string_to_number(char):
    if char.isnumeric():
        return int(char)
    if char.isalpha():
        return ord(char) - 55
    return -1


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    print("Number =", string_to_number(string_input))
