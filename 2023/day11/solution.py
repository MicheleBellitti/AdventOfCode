"""
Advent of Code 2023
Day 11
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
import numpy as np
from utils.advent import *
from itertools import combinations


def expand(grid):
    new_grid = []

    for row in grid:
        new_grid.append(row)
        if '#' not in row:
            
            new_grid.append(row)
    for c in range(len(grid[0])):
        if all(row[c] != '#' for row in grid):
            for row in new_grid:
                row = row[:c] + row[c] + row[c:]
    return new_grid

def get_galaxies(grid):
    return [(i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == '#']
        
            
        

def p1(inp):
    # grid = expand(inp)
    grid = inp
    empty_rows = [i for i, row in enumerate(grid) if '#' not in row]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch != '#' for ch in col)]
    
    galaxies = get_galaxies(grid)
    total = 0
    scale = 2
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            for r in range(min(r1, r2), max(r2, r1)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c2, c1)):
                total += scale if c in empty_cols else 1
    return total   
def p2(inp):
    grid = inp
    empty_rows = [i for i, row in enumerate(grid) if '#' not in row]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch != '#' for ch in col)]
    
    galaxies = get_galaxies(grid)
    total = 0
    scale = 1e6
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            for r in range(min(r1, r2), max(r2, r1)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c2, c1)):
                total += scale if c in empty_cols else 1
    return total  
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    # print(inp)
    
    # code
    p_1, p_2 = p1(inp.splitlines()), p2(inp.splitlines())
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 11
    
    setup(y, d)
    
    # Process and output result
    print("Solution:", process_input(y, d))

