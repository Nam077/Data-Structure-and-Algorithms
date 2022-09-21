def check_uppercase(string):
    for char in string:
        if char.islower():
            return False
        if char.isnumeric():
            return False
    return True


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    if check_uppercase(string_input):
        print("Yes")
    else:
        print("No")
