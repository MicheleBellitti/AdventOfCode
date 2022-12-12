import collections
import math
from time import sleep

import numpy as np


# Shortest path algoritm
def shortest_path(grid, start):
    queue = collections.deque([(start, 0)])
    visited = set()
    while queue:
        (x, y), dist = queue.popleft()

        if grid[x, y] == 'E':
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):

            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                b = grid[x2, y2].replace('E', 'z')
                a = grid[x, y].replace('S', 'a')
                if ord(b) - ord(a) <= 1:
                    queue.append(((x2, y2), dist + 1))


grid = [[a for a in line.replace('\n', '')] for line in open('input#12.txt', 'r').readlines()]
grid = np.array(grid)
start = np.where(grid == 'S')[0][0], np.where(grid == 'S')[1][0]
dists = []

# Part 1
dist_1 = shortest_path(grid, start)
starts = list()
starts.extend([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i, j] == 'a'])

# Part 2
for s in starts:
    d = shortest_path(grid, s)
    dists.append(d) if d else None

# printing results
print(f'part 1: {dist_1}\t|\tpart 2: {min(dists)}.')
