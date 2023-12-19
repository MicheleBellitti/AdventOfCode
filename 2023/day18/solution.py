"""
Advent of Code 2023
Day 18
Author: Michele
"""
import os
from datetime import datetime
import pprint
from aocd import get_data, submit
from utils.advent import *
from itertools import combinations


def p1(inp):
    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    b = 0

    for line in inp:
        d, n, _ = line
        dr, dc = dirs[d]
        n = int(n)
        b += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1
    return i+b

def p2(inp):
    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    b = 0

    for line in inp:
        _, _, x = line
        x = x[2:-1]
        dr, dc = dirs["RDLU"[int(x[-1])]]
        n = int(x[:-1], 16)
        b += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1

    return i+b
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read().splitlines()
    inp = [l.strip().split() for l in inp]
    # inp = get_data(day=day, year=year)
    # print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 18
    
    setup(y, d)
    
    # Process and output result
    print("Solution:", process_input(y, d))

