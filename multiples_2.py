def multiples_2(a, b, m):
    count = 0
    for i in range(a, b):
        if i % m == 0:
            count += 1
    return count


if __name__ == '__main__':
    print("Enter a: ")
    a_input = int(input())
    print("Enter b: ")
    b_input = int(input())
    print("Enter m: ")
    m_input = int(input())
    print("Number of multiples =", multiples_2(a_input, b_input, m_input))
