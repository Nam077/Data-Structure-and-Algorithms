from typing import Any


class Result:
    def __int__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds


def time_conversion_2(seconds):
    minute_result: int | Any = seconds // 60
    second_result = seconds % 60
    result = Result()
    result.minutes = minute_result
    result.seconds = second_result
    return result


if __name__ == '__main__':
    print('Enter seconds: ')
    s = 0
    try:
        s = int(input())
    except ValueError:
        print('Please enter a number')
    result_work = time_conversion_2(s)
    print('Time : ', result_work.minutes, 'minutes and', result_work.seconds, 'seconds')
