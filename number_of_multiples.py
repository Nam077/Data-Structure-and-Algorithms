def number_of_multiples(n: int, m: int):
    count = 0
    for i in range(1, n):
        if i % m == 0:
            count += 1
    return count


if __name__ == '__main__':
    print("Enter n: ")
    n_input = int(input())
    print("Enter m: ")
    m_input = int(input())
    print("Number of multiples =", number_of_multiples(n_input, m_input))
