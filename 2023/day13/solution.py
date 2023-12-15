"""
Advent of Code 2023
Day 13
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return r
        
    return 0

def find_mirror2(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

def p1(inp):
    ans = 0

    for block in inp.split("\n\n"):
        grid = block.splitlines()

        row = find_mirror(grid)
        ans += row * 100

        col = find_mirror(list(zip(*grid)))
        ans += col

    return ans


def p2(inp):
    ans = 0
    for block in inp.split("\n\n"):
        grid = block.splitlines()

        row = find_mirror(grid)
        ans += row * 100

        col = find_mirror2(list(zip(*grid)))
        ans += col
    
    return ans


def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    # print(inp)

    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)

    return p_1, p_2


if __name__ == "__main__":
    y = datetime.now().year
    d = 13

    setup(y, d)

    # Process and output result
    print("Solution:", process_input(y, d))
