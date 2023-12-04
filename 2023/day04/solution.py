"""
Advent of Code 2023
Day 4
Author: Michele
"""

def p1(inp):
    points = [0 for _ in range(len(inp))]
    inp = [i.split(' | ') for i in inp]
    # print(inp)
    for index, card in enumerate(inp):
        winning, guesses = set(map(int, card[0][card[0].find(':')+1:].split())), set(map(int, card[1].split()))
        # print(len(winning & guesses))
        
        points[index] = int(2**(len(winning & guesses) - 1))
    return sum(points)

def p2(inp):
    points = [1 for _ in range(len(inp))]
    inp = [i.split(' | ') for i in inp]
    
    
    for index, card in enumerate(inp):
        winning, guesses = set(map(int, card[0][card[0].find(':')+1:].split())), set(map(int, card[1].split()))
        # print(len(winning & guesses))
        
        copies = len(winning & guesses)
        for j in range(1,copies+1):
            if index+j < len(points):
                points[index+j] += points[index]
        # print(index, copies)
        
        # print(points)
    return sum(points)


def process_input():
    inp = open(0, encoding='utf-8').read().splitlines()
    
    # code
    return f"Part 1: {p1(inp)}\tPart 2: {p2(inp)}"
    
if __name__ == "__main__":
    

    # Process and output result
    print("Solution:", process_input())

