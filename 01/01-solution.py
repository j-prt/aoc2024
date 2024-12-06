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


def solve_1(data):
    data = preprocess(data)
    return reduce(reducer, data, 0)


# Get the solution for part 1
data = load(INPUT_PATH)
solution_1 = solve_1(data)
print(solution_1)
