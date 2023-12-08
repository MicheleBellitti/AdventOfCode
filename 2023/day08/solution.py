"""
Advent of Code 2023
Day 8
Author: Michele
"""
import math
import os
from datetime import datetime
from aocd import get_data, submit
import utils
from utils.advent import check_setup_once, log, logcont, check_or_die, setup, suppress



def explore(start, graph, instructions):
    curr = start
    steps = 0
    while True:
        
        # print(curr)
        if curr.endswith("Z"):
            break
        for dir in instructions:
            curr = graph[curr][0] if dir == 'L' else graph[curr][1]
            steps += 1
            # print(curr)
    return steps


def p1(graph, instructions):
    start = "AAA"
    end = "ZZZ"
    # build a graph
    
    
    # print(graph)
    return explore(start, graph, instructions)
def p2(graph, instructions, starts):
    steps = 0
    curr = starts
    print(f"Starts: {starts}")
    
    lcms = [explore(start, graph, instructions) for start in starts]
    return math.lcm(*lcms)

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    
    graph  = dict()
    instructions, nodes = inp.split("\n\n")
    starts = []
    for node in nodes.splitlines():
        
        start, neighbors = node.split(" = ")
        if start.endswith("A") and start not in starts:
            starts.append(start)
        l, r = neighbors.split(", ")
        graph[start] = (l[1:], r[:-1])
    # code
    p_1 = p1(graph, instructions)
    p_2 = p2(graph, instructions, starts)
    submit(p_2, part='b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 8
    
    setup(y, d)
    # Process and output result
    print("Solution:", process_input(y, d))

