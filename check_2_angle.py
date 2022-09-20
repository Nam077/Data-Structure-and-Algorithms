def check_two_angle(first, second):
    if first < 0 or second < 0 or first + second > 180:
        return False
    return True


if __name__ == '__main__':
    print("Enter angle first: ")
    angle_first = 0
    try:
        angle_first = int(input())
    except ValueError:
        print('Please enter a number')
    print("Enter angle second :")
    angle_second = 0
    try:
        angle_second = int(input())
    except ValueError:
        print('Please enter a number')
    if check_two_angle(angle_first, angle_second):
        print("Yes")
    else:
        print("No")
