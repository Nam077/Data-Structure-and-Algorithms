def check_balance(a, b, c, d):
    if a + b == c + d:
        return True
    if a + c == b + d:
        return True
    if a + d == b + c:
        return True
    return False


if __name__ == '__main__':
    print("Enter a: ")
    a, b, c, d = 0, 0, 0, 0
    try:
        a = int(input())
    except ValueError:
        print('Please enter a number')

    print("Enter b: ")
    try:
        b = int(input())
    except ValueError:
        print('Please enter a number')

    print("Enter c: ")
    try:
        c = int(input())
    except ValueError:
        print('Please enter a number')

    print("Enter d: ")
    try:
        d = int(input())
    except ValueError:
        print('Please enter a number')

    if check_balance(a, b, c, d):
        print("Yes")
    else:
        print("No")
