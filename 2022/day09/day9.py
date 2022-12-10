import numpy as np
from copy import deepcopy

moves = [line.replace('\n', '').split(' ') for line in open('input#9.txt', 'r').readlines()]
grid_dim = max([int(move[1]) for move in moves])
grid = np.array([['.' for _ in range(grid_dim+1)] for _ in range(grid_dim+1)])


tails = set()
seen = set()

knots = [deepcopy([0, 0]) for _ in range(10)]


def sign(a, b):
    return (a - b) // abs(a - b)


def update_pos(tail, head, is_last=False):
    while abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
        # print(grid)
        if tail[0] == head[0]:
            tail[1] += sign(head[1], tail[1])
        elif tail[1] == head[1]:
            tail[0] += sign(head[0], tail[0])
        else:
            tail[0] += sign(head[0], tail[0])
            tail[1] += sign(head[1], tail[1])
        tails.add(tuple(tail))
        if is_last:
            seen.add(tuple(knots[-1]))


def part1():
    T = deepcopy([len(grid) - 1, 0])
    H = deepcopy([len(grid) - 1, 0])
    for m, d in moves:
        d = int(d)
        if m == 'U':
            H = [H[0] - d, H[1]]
            update_pos(T, H)
        elif m == 'D':
            H = [H[0] + d, H[1]]
            update_pos(T, H)
        elif m == 'L':
            H = [H[0], H[1] - d]
            update_pos(T, H)
        elif m == 'R':
            H = [H[0], H[1] + d]
            update_pos(T, H)
    return len(tails)


def update_knots(knots):
    for i in range(1, len(knots)):
        is_last = i == len(knots) - 1

        update_pos(knots[i], knots[i - 1], is_last)


def part2():
    # First knot is the rope's head, last one is the tail
    seen.add(tuple(knots[-1]))
    for m, d in moves:
        deltas = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        d = int(d)
        dx, dy = deltas[m]

        for _ in range(d):
            knots[0] = deepcopy([knots[0][0] + dx, knots[0][1] + dy])
            update_knots(knots)

    return len(seen)


print(f'Part 1:{part1()}\t|\tPart 2: {part2()}')
