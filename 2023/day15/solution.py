"""
Advent of Code 2023
Day 15
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *
import re

# Solution here

def hash_fn(s:str):
    ans = 0
    for ch in s:
        ans += ord(ch)
        ans *= 17
        ans %= 256
    return ans

def p1(inp):
    ret = 0
    for s in inp.split(','):
        # print(s)
        ret += hash_fn(s)
    return ret

def get_index(box:list, label:str):
    i = -1 # -1 means not found but this should never happen
    for j, lens in enumerate(box):
        if label in lens:
            i = j
            break
    return i

def p2(inp):
    boxes = [[] for _ in range(256)]
    for s in inp.split(','):
        if '-' in s:
            lab = s[:-1]
            index = hash_fn(lab)
            
            if any(lab in lens for lens in boxes[index]):
                i = get_index(boxes[index], lab)
                boxes[index].remove(boxes[index][i])
                # print(f'removed {lab} from box: {index}')
                # print(boxes[index])
        else:
            lab, focal = s.split('=')
            focal = int(focal)
            index = hash_fn(lab)
            # print(lab, index)
            if any(lab in lens for lens in boxes[index]):
                i = get_index(boxes[index], lab)
                boxes[index][i][1] = focal
                # print(f'updated {lab} in box: {index} with focal {focal}')
            else:
                boxes[index].append([lab, focal])
                # print(f'added {lab} to box: {index}')
            # print(boxes[index])
                
    # print(boxes)
    score = 0
    for i, box in enumerate(boxes):
        for j, (_, focal) in enumerate(box):
            score += (i + 1) * focal * (j + 1) 
    return score
            
    

def process_input(year, day):
    inp = open(0).read()
    # inp = get_data(day=day, year=year)
    # print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 15
    
    setup(y, d)
    
    # Process and output result
    print("Solution:", process_input(y, d))





