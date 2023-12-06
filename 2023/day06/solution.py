"""
Advent of Code 2023
Day 6
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
import math
# Solution here

def p1(inp):
    ways = []
    times, distances = inp.splitlines(keepends=False)


    times, distances = list(map(int, times[times.find(":")+1:].split())), list(map(int, distances[distances.find(":")+1:].split()))
    # print(times, distances)
    ways.extend(
        sum(bool(i * (time - i) > dist)
        for i in range(time))
        for time, dist in zip(times, distances)
    )
    # print(ways)
    return math.prod(ways)

def p2(inp):

    times, distances = inp.splitlines(keepends=False)


    times, distances = times[times.find(":")+1:].split(), distances[distances.find(":")+1:].split()
    time, dist = int(''.join(times)), int(''.join(distances))

    return sum(i * (time - i) > dist for i in range(time))
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    print("input: ")
    print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 6
    
    # Process and output result
    print("Solution:", process_input(y, d))

