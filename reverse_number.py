def reverse_number(number: int):
    return int(str(number)[::-1]) + number


if __name__ == '__main__':
    print("Enter number: ")
try:
    number_input = int(input())
    print("Sum =", reverse_number(number_input))
except ValueError:
    print("Error: Input is not a number")
