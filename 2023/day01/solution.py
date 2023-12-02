"""
Advent of Code 2023
Day 1
Author: Michele
"""
import re
alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def p1(inp):
    calibration = 0
    for l in inp:
        cs = re.findall(r"(\d+)", l)
        # print(cs)
        
        calibration += int(f"{int(cs[0][0])}{int(cs[-1][-1])}")
    return calibration

def filt(line):
        for i, n in enumerate(alpha):
            line.replace(n, n+str(i+1)+n)
        x = re.findall(r'(\d)', line)
        # print(x)
        return int(x[0][0] + x[-1][-1])
    
def p2(inp):
    return sum(map(filt, inp))

def process_input():
    inp = open(0, encoding='utf-8 ').read().splitlines()
    # print(inp)
    
    return f"Part 1: {p1(inp)}\tPart 2: {p2(inp)}"
    
if __name__ == "__main__":
    # Process and output result
    print("Solution:", process_input())

