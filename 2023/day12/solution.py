"""
Advent of Code 2023
Day 13
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result


def p1(inp, fn=count):
    
    ans = 0

    for line in inp:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        ans += fn(cfg, nums)

    return ans

def p2(inp):
    ans = 0

    for line in inp:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        
        cfg = "?".join([cfg] * 5)
        nums *= 5
        
        ans += count(cfg, nums)
    
    return ans


def process_input(year, day):
    inp = open(0, encoding='utf-8').read().splitlines()
    # inp = get_data(day=day, year=year)
    print(inp)

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
