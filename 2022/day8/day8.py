import numpy as np


lines = [line.strip().replace('\n', '') for line in open("input#8.txt").readlines()]

lines = np.array([[int(x) for x in line] for line in lines])


# repeats = np.array([[0 for _ in range(len(lines[0]))] for _ in range(len(lines))])


def check_edges(x, y):
    return x == 0 or x == len(lines) - 1 or y == 0 or y == len(lines[0]) - 1


def is_visible(x, y):
    # print(lines[x, y],lines[:x, y], lines[x + 1:, y], lines[x, :y], lines[x, y + 1:])
    if all(lines[x, y] > a for a in lines[x + 1:, y]) or all(lines[x, y] > b for b in lines[:x, y]) or all(
            lines[x, y] > c \
            for c in lines[x, y + 1:]) or all(lines[x, y] > d for d in lines[x, :y]):
        return True


def part1():
    visible_from_outside = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):

            if check_edges(i, j):

                visible_from_outside += 1
            elif is_visible(i, j):

                visible_from_outside += 1

    return visible_from_outside


def part2():
    dists = []
    p2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):

            length = len(lines)
            width = len(lines[0])
            dirs = []
            current = lines[i, j]
            for func in (
                    lambda y, x: (y - 1, x), lambda y, x: (y + 1, x), lambda y, x: (y, x - 1), lambda y, x: (y, x + 1)):
                a, b = i, j
                s = 0
                while True:
                    b, a = func(b, a)
                    if c := (0 <= a < length and 0 <= b < width):

                        s += 1
                    if not c or int(lines[a][b]) >= current:
                        dirs.append(s)
                        break
            p2 = max(p2, dirs[0] * dirs[1] * dirs[2] * dirs[3])
            dists.append(p2)
    return max(dists)


print(f'part 1: {part1()}\t|\tpart 2: {part2()}')
