"""
Advent of Code 2023
Day 6
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit

# Solution here

def p1(inp):
    pass
def p2(inp):
    pass
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = int(input("Enter the day: "))
    
    # Process and output result
    print("Solution:", process_input(y, d))

