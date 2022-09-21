def reverse_string(string):
    return string[::-1]


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    print("Reverse string =", reverse_string(string_input))
