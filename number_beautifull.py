def number_beautiful(number):
    str_number = str(number)
    for i in range(1, len(str_number) - 1):
        if str_number[i] != str_number[i - 1]:
            return False
        return True


if __name__ == '__main__':
    print("Enter number: ")
    try:
        number_input = int(input())
        print("Number =", number_beautiful(number_input))
    except ValueError:
        print("Error: Input is not a number")
