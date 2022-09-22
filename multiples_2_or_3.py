def multiples_2_or_3(n):
    count = 0
    for i in range(1, n):
        if i % 2 == 0 or i % 3 == 0:
            count += 1
    return count


if __name__ == '__main__':
    print("Enter n: ")
    n_input = int(input())
    print("Number of multiples =", multiples_2_or_3(n_input))
