"""
Advent of Code 2023
Day 19
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *

# Solution here

def p1(inp):
    block1, block2 = inp.split("\n\n")

    workflows = {}

    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    ops = {
        ">": int.__gt__,
        "<": int.__lt__
    }

    def accept(item, name = "in"):
        if name == "R":
            return False
        if name == "A":
            return True

        rules, fallback = workflows[name]
        
        for key, cmp, n, target in rules:
            if ops[cmp](item[key], n):
                return accept(item, target)
        
        return accept(item, fallback)

    total = 0

    for line in block2.splitlines():
        item = {}
        for segment in line[1:-1].split(","):
            ch, n = segment.split("=")
            item[ch] = int(n)
        if accept(item):
            total += sum(item.values())
    return total
def p2(inp):
    block1, _ = inp.split("\n\n")

    workflows = {}

    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    def count(ranges, name = "in"):
        if name == "R":
            return 0
        if name == "A":
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product
        
        rules, fallback = workflows[name]

        total = 0

        for key, cmp, n, target in rules:
            lo, hi = ranges[key]
            if cmp == "<":
                T = (lo, min(n - 1, hi))
                F = (max(n, lo), hi)
            else:
                T = (max(n + 1, lo), hi)
                F = (lo, min(n, hi))
            if T[0] <= T[1]:
                copy = dict(ranges)
                copy[key] = T
                total += count(copy, target)
            if F[0] <= F[1]:
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else:
            total += count(ranges, fallback)
                
        return total

    return count({key: (1, 4000) for key in "xmas"})
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    # print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 19
    
    setup(y, d)
    
    # Process and output result
    print("Solution:", process_input(y, d))

