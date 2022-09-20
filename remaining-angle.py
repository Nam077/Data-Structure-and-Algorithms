def remaining_angle(first, second):
    return 180 - first - second


if __name__ == '__main__':
    angle_second, angle_first = 0, 0
    print("Enter angle first: ")
    try:
        angle_first = int(input())
    except ValueError:
        print('Please enter a number')

    print("Enter angle second :")
    try:
        angle_second = int(input())
    except ValueError:
        print('Please enter a number')
    print("Remaining angle :", remaining_angle(angle_first, angle_second))
