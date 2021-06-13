import re


def calculator(func, *numbers):
    result: int = 0

    for number in numbers:
        result += func(number)

    return result


def filters(numbers: list, func):
    evens = []
    for number in numbers:
        if func(number):
            evens.append(number)
    return evens


if __name__ == '__main__':
    total = calculator(lambda number: number * 2, 1, 2, 3, 4, 10)
    print(total)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filters(numbers, lambda num: num % 2 == 1))
