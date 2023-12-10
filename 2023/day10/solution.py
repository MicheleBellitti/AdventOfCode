"""
Advent of Code 2023
Day 10
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *
from collections import deque


# Solution here
def bfs(grid, start):
    q = [start]
    visited = {start}
    while q:
        curr = q.pop(0)
        r, c = curr
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            q.append((r - 1, c))

        if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            q.append((r + 1, c))

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            q.append((r, c - 1))

        if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in visited:
            visited.add((r, c + 1))
            q.append((r, c + 1))

    # print(visited)
    return len(visited) // 2


def p1(inp):
    sx, sy = {
        (x, y) for x in range(len(inp)) for y in range(len(inp[0])) if inp[x][y] == "S"
    }.pop()
    start = (sx, sy)
    print(f"start: {start}")
    return bfs(inp, start)

def bfs_2(grid, start):
    maybe_s = {"|", "-", "J", "L", "7", "F"}
    visited = set()
    visited.add(start)
    q = deque([start])
    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            q.append((r - 1, c))
            if ch == "S":
                maybe_s &= {"|", "J", "L"}

        if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            q.append((r + 1, c))
            if ch == "S":
                maybe_s &= {"|", "7", "F"}

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            q.append((r, c - 1))
            if ch == "S":
                maybe_s &= {"-", "J", "7"}

        if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in visited:
            visited.add((r, c + 1))
            q.append((r, c + 1))
            if ch == "S":
                maybe_s &= {"-", "L", "F"}

    assert len(maybe_s) == 1
    (S,) = maybe_s

    grid = [row.replace("S", S) for row in grid]
    grid = ["".join(ch if (r, c) in visited else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

    outside = set()

    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch != ".":
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))

    return len(grid) * len(grid[0]) - len(outside | visited)


def p2(inp):
    sx, sy = {
        (x, y) for x in range(len(inp)) for y in range(len(inp[0])) if inp[x][y] == "S"
    }.pop()
    start = (sx, sy)
    print(f"start: {start}")
    return bfs_2(inp, start)

def process_input(year, day):
    inp = open(0, encoding="utf-8").read()
    # inp = get_data(day=day, year=year)
    print(inp)

    # code
    p_1, p_2 = p1(inp.splitlines()), p2(inp.splitlines())
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)

    return p_1, p_2


if __name__ == "__main__":
    y = datetime.now().year
    d = 10

    setup(y, d)

    # Process and output result
    print("Solution:", process_input(y, d))
