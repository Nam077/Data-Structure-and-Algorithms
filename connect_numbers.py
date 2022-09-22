def connect_numbers(number1, number2):
    return int(str(number1) + str(number2)) * 2


if __name__ == '__main__':
    number_1 = 0
    number_2 = 0
    print("Enter number 1: ")
    try:
        number_1 = int(input())
    except ValueError:
        print("Error: Input is not a number")
    print("Enter number 2: ")
    try:
        number_2 = int(input())
    except ValueError:
        print("Error: Input is not a number")
    print("Sum =", connect_numbers(number_1, number_2))
