import math


def number_of_vases(v, n):
    count = math.floor(n / v)
    if count * v < n:
        count += 1
    return count


if __name__ == '__main__':
    print("Enter v: ")
    v_input = int(input())
    print("Enter n: ")
    n_input = int(input())
    print("Number of vases =", number_of_vases(v_input, n_input))
