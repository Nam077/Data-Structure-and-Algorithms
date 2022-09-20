class Result:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def value_swap(a, b):
    temp = a
    a = b
    b = temp
    return Result(a, b)


if __name__ == '__main__':
    print("Enter a: ")
    a = 0
    try:
        a = int(input())
    except ValueError:
        print('Please enter a number')
    print("Enter b :")
    b = 0
    try:
        b = int(input())
    except ValueError:
        print('Please enter a number')
    result_work = value_swap(a, b)
    print("a =", result_work.a, "b =", result_work.b)
