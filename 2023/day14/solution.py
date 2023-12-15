"""
Advent of Code 2023
Day 14
Author: Michele
"""

import itertools
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *


def cycle(grid):
    for _ in range(4):
        grid = tilt(grid)
        grid = rotate(grid)
    return grid


def tilt(grid):

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                i, j = r, c
                
                while i > 0 and grid[i - 1][j] == ".":
                    i -= 1
                grid[r][c] = "."
                grid[i][j] = "O"

    return grid

def rotate(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = [["." for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            new_grid[j][n - i - 1] = grid[i][j]
    return new_grid
def p1(inp):
    grid = tilt(inp)

    load = 0  # noqa: F841
    n = len(inp)  # noqa: F841
    print()

    return score(grid)

def score(grid):
    load = 0
    n = len(grid)
    for r, row in enumerate(grid):
        load += sum(n - r for c in row if c == "O")
    return load

def apply_n_times(f, x, n):
    """
    Apply `f` to `x` `n` times, returning the result.
    Assumes `f` is deterministic and takes one hashable argument.
    Saves time by finding the first cycle, calculating its length, and using that to skip ahead.
    """
    seen = {}
    for i in range(n):
        t = ''.join(''.join(row) for row in x)
        if t in seen:
            break
        seen[t] = i
        x = f(x)
    else:
        return x

    cycle_start = seen[t]
    cycle_len = i - cycle_start
    remaining = (n - i) % cycle_len
    return apply_n_times(f, x, remaining)


def p2(inp, iterations=int(1e9)):
    final = apply_n_times(cycle, inp, iterations)
    return score(final)


def process_input(year, day):
    inp = open(0, encoding="utf-8").read()
    # inp = get_data(day=day, year=year)
    # print(inp)

    # code
    inp = inp.splitlines()
    inp = [[c for c in l] for l in inp]
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part="a", day=day, year=year)
    submit(p_2, part="b", day=day, year=year)

    return p_1, p_2


if __name__ == "__main__":
    y = datetime.now().year
    d = 14

    setup(y, d)

    # Process and output result
    print("Solution:", process_input(y, d))
