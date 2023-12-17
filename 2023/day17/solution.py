"""
Advent of Code 2023
Day 17
Author: Michele
"""
import os
from datetime import datetime
from aocd import get_data, submit
from utils.advent import *
from heapq import heappush, heappop
import pprint

def print(v):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(v)

# Solution here

def p1(grid):
    
    q = [(0, 0, 0, 0, 0, 0)]
    seen = set()
    m, n = len(grid), len(grid[0])
    directions = {'R':(0, 1), 'L':(0, -1), 'D':(1, 0), 'U':(-1, 0)}
    
    while q:
        heat_loss, x, y, dx, dy, hops = heappop(q)
        
        if (x, y, dx, dy, hops) in seen:
            continue
        
        if (x, y) == (m-1, n-1):
            return heat_loss
        
        seen.add((x, y, dx, dy, hops))
        
        if hops < 3 and (dx, dy) != (0, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n:
                heappush(q, (heat_loss+grid[nx][ny], nx, ny, dx, dy, hops+1))
        
        for ndr, ndc in directions.values():
            
            if(dx, dy) != (ndr, ndc) and (ndr, ndc) != (-dx, -dy):
                if 0 <= x+ndr < m and 0 <= y+ndc < n:
                    heappush(q, (heat_loss+grid[x+ndr][y+ndc], x+ndr, y+ndc, ndr, ndc, 1))
            
            
        

def p2(grid):
    
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
            return hl
            

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
                        
def process_input(year, day):
    inp = open(0, encoding='utf-8').read().splitlines()
    
    inp = [[int(x) for x in line] for line in inp]
    # inp = get_data(day=day, year=year)
    #print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    print((p_2))
    submit(p_1, part='a', day=day, year=year)
    submit(p_2, 'b', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = 17
    
    setup(y, d)
    
    # Process and output result
    print("Solution: ")
    
    process_input(y, d)

