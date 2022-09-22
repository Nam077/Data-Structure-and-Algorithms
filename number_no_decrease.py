def number_no_decrease(number):
    str_number = str(number)
    for i in range(1, len(str_number) - 1):
        if int(str_number[i]) < int(str_number[i - 1]):
            return False
    return True


if __name__ == '__main__':
    print("Enter number: ")
    try:
        number_input = int(input())
        print("Number =", number_no_decrease(number_input))
    except ValueError:
        print("Error: Input is not a number")
