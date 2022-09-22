def number_of_0_at_end(number):
    str_number = str(number)
    count = 0
    for element in str_number[::-1]:
        if element != '0':
            return count
        if element == '0':
            count += 1
    return count


if __name__ == '__main__':
    print("Enter number: ")
    number_input = int(input())
    print("Number of 0 at end =", number_of_0_at_end(number_input))
