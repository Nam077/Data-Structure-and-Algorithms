def time_conversion(minutes, seconds):
    return minutes * 60 + seconds


if __name__ == '__main__':
    print('Enter minutes: ')
    m, s = 0, 0
    try:
        m = int(input())
    except ValueError:
        print('Please enter a number')

    print('Enter seconds: ')
    try:
        s = int(input())
    except ValueError:
        print('Please enter a number')
    print('Time in seconds: ', time_conversion(m, s))
