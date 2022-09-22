import math


def square_number_2(number: int):
    for i in range(1, number + 1):
        if check_square_number(i * number):
            return i


def check_square_number(number: int):
    sqr = math.sqrt(number)
    if sqr * sqr == number:
        return True
    return False


if __name__ == '__main__':
    print("Enter number: ")
    try:
        number_input = int(input())
        print("Number =", square_number_2(number_input))
    except ValueError:
        print("Error: Input is not a number")
