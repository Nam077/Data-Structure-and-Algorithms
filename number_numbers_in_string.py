def number_numbers_in_string(string):
    number = 0
    for char in string:
        if char.isnumeric():
            number += 1
    return number


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    print("Number of numbers =", number_numbers_in_string(string_input))
