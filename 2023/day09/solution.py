"""
Advent of Code 2023
Day 9
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *
from itertools import pairwise

# Solution here
def extrapolate(sequence):
        extrapolated = sequence[-1]
        while True:
            sequence = [j - i for i, j in pairwise(sequence)]
            # print(sequence)
            if sequence:
                extrapolated += sequence[-1]
            if all(n == 0 for n in sequence):
                break
        return extrapolated
            
def p1(inp):
    vals = 0
    for seq in inp:
        
        
        v = extrapolate(seq)
        
        vals += v
        
    return vals
def p2(inp):
    
    vals = 0
    for seq in inp:
        
        
        v = extrapolate(seq[::-1])
        
        vals += v
        
    return vals
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    history = [list(map(int, line.split())) for line in inp.splitlines()]
    # print(history)
    
    # code
    p_1, p_2 = p1(history), p2(history)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 9
    
    setup(y, d)
    
    # Process and output result
    print("Solution:", process_input(y, d))

