# https://adventofcode.com/2024/day/1

from functools import reduce

INPUT_PATH = '01-input.txt'


def load(path: str):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    return data


def dist(a: int, b: int):
    return abs(a - b)


def reducer(acc: int, cur: tuple[int, int]):
    return acc + dist(*cur)


def preprocess(data):
    # Split, convert to ints, sort, zip
    a, b = [], []

    for line in data:
        left, right = line.split('   ')
        a.append(int(left))
        b.append(int(right))

    a.sort()
    b.sort()

    return zip(a, b)


# Most expensive ops are the sorts. O(nlogn)
def solve_1(data):
    data = preprocess(data)
    return reduce(reducer, data, 0)


# Get the solution for part 1
data = load(INPUT_PATH)
solution_1 = solve_1(data)
print(solution_1)


# Start part 2
def preprocess_2(data):
    # Split, convert to ints
    a, b = [], []

    for line in data:
        left, right = line.split('   ')
        a.append(int(left))
        b.append(int(right))

    return a, b


# Brute force, nothing clever to see here. O(n^2)
def solve_2(data: tuple[list[int], list[int]]):
    left, right = preprocess_2(data)
    total = 0

    for el in left:
        value = el * right.count(el)
        total += value

    return total


solution_1 = solve_2(data)
print(solution_1)
