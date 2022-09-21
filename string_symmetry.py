def string_symmetry(string):
    check = True
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            check = False
    return check


if __name__ == '__main__':
    print("Enter string: ")
    string_input = input()
    print("Symmetry =", string_symmetry(string_input))
