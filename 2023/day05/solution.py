"""
Advent of Code 2023
Day 5
Author: Michele
"""
# Your solution here

import math
from aocd import *

def p1(inp):
    blocks = inp.split("\n\n")
    seeds = list(map(int, blocks[0][blocks[0].find(":") + 1 :].strip().split(" ")))
    maps = [
        list(
            map(int, block[block.find(":") + 1 :].strip().replace("\n", " ").split(" "))
        )
        for block in blocks[1:]
    ]

    locations = []
    for seed in seeds:
        loc = seed
        for line in maps:
            for ind in range(0, len(line), 3):
                dst, src, size = line[ind], line[ind + 1], line[ind + 2]
                if loc in range(src, src + size):
                    loc = dst + (loc - src)
                    break # correct mapping found
        locations.append(loc)
    return min(locations)

def p2(inp):
    blocks = inp.split("\n\n")
    seed_ranges = list(map(int, blocks[0][blocks[0].find(":") + 1 :].strip().split(" ")))
    maps = [
        list(
            map(int, block[block.find(":") + 1 :].strip().replace("\n", " ").split(" "))
        )
        for block in blocks[1:]
    ]

    locations = []
    for i in range(0, len(seed_ranges), 2):
        start_seed = seed_ranges[i]
        range_length = seed_ranges[i + 1]

        for seed in range(start_seed, start_seed + range_length):
            loc = seed
            for line in maps:
                for ind in range(0, len(line), 3):
                    dst, src, size = line[ind], line[ind + 1], line[ind + 2]
                    if loc in range(src, src + size):
                        loc = dst + (loc - src)
                        break  # Break the loop once the correct mapping is found
            locations.append(loc)

    return min(locations)

def process_input():
    inp = open(0, encoding="utf-8 ").read()
    return f"Part 1: {p1(inp)}\nPart 2: {p2(inp)}"


if __name__ == "__main__":
    # Process and output result
    print("Solution:", process_input())



if __name__ == "__main__":
    # Process and output result
    print("Solution:", process_input())

