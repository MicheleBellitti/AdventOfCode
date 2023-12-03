"""
Advent of Code 2023
Day 3
Author: Michele
"""
import re
import math as m


def process_grid(board):
    board_length = len(board)
    chars = {
        (r, c): []
        for r in range(board_length)
        for c in range(board_length)
        if board[r][c] not in "01234566789."
    }

    for r, row in enumerate(board):
        for n in re.finditer(r"\d+", row):
            edge = {
                (r, c)
                for r in (r - 1, r, r + 1)
                for c in range(n.start() - 1, n.end() + 1)
            }

            for o in edge & chars.keys():
                chars[o].append(int(n.group()))
    return chars

def solve(inp):
    board = list(inp)
    chars = process_grid(board)
    
    return f"Part 1: {sum(sum(p) for p in chars.values())}\t Part 2: {sum(m.prod(p) for p in chars.values() if len(p) == 2)}"




def process_input():
    inp = open(0, encoding='utf-8 ')
    # code
    return f"{solve(inp)}"
    
if __name__ == "__main__":

    # Process and output result
    print("Solution:", process_input())

