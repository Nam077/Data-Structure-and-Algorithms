def unique_number(arr):
    array_number = []
    for number in arr:
        if number not in array_number:
            array_number.append(number)
            count = 0
            for number2 in arr:
                if number == number2:
                    count += 1
            if count > 1:
                array_number.remove(number)
    if len(array_number) < 1:
        return "Not found"
    number_return = array_number[0]
    for i in range(1, len(array_number)):
        if array_number[i] > number_return:
            number_return = array_number[1]
    return number_return


print(unique_number([3, 4, 4, 3]))
