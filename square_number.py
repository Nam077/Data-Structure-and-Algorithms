def find_square_nearest(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i


def find_number(n):
    return find_square_nearest(n) - n


if __name__ == '__main__':
    print("Enter number: ")
    number_input = int(input())
    print("Number =", find_number(number_input))
