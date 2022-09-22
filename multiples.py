def multiples(n, m):
    multiples_arr = []
    for i in range(1, n):
        if i % m == 0:
            multiples_arr.append(i)
    return multiples_arr


if __name__ == '__main__':
    print("Enter n: ")
    n_input = int(input())
    print("Enter m: ")
    m_input = int(input())
    print("Multiples =", multiples(n_input, m_input))
