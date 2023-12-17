"""
Advent of Code 2023
Day 16
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *
from collections import deque


def explore(grid, init=(0, -1, 0, 1)):
    
    a = [init]
    seen = set()
    q = deque(a)

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        ch = grid[r][c]
        
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
                    
    coords = {(r, c) for (r, c, _, _) in seen}

    return len(coords)


def p1(inp):
    return explore(inp)


def p2(inp):
    max_val = 0

    for r in range(len(inp)):
        max_val = max(max_val, explore(inp, (r, -1, 0, 1)))
        max_val = max(max_val, explore(inp, (r, len(inp[0]), 0, -1)))
        
    for c in range(len(inp)):
        max_val = max(max_val, explore(inp, (-1, c, 1, 0)))
        max_val = max(max_val, explore(inp, (len(inp), c, -1, 0)))

    return max_val


def process_input(year, day):
    inp = open(0, encoding="utf-8").read()
    # inp = get_data(day=day, year=year)
    print(inp)

    # code
    p_1, p_2 = p1(inp.splitlines()), p2(inp)
    submit(p_1, part="a", day=day, year=year)
    submit(p_2, part="b", day=day, year=year)

    return p_1, p_2


if __name__ == "__main__":
    y = datetime.now().year
    d = 16

    setup(y, d)

    # Process and output result
    print("Solution:", process_input(y, d))
