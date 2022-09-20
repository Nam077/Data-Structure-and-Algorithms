def sum_1(n):
    s = 0
    for i in range(1, n + 1):
        s += ((-1) ** i) * i
    return s


if __name__ == '__main__':
    print("Enter n: ")
    n = 0
    try:
        n = int(input())
    except ValueError:
        print('Please enter a number')
    print("Sum =", sum_1(n))
