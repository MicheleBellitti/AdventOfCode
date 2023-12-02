"""
Advent of Code 2023
Day 2
Author: Michele
"""
import re

"""
part 1: 2528
part 2: 67363

"""

bag = {"red": 12, "blue": 14, "green": 13}


def p1(inp):
    games = [[0, 0, 0] for i in range(len(inp))]
    ids = []
    valid = 0
    for i in range(len(inp)):
        sets = inp[i]
        #print(sets)
        for s in sets:
            # print(s)
            games[i] = [
                sum(list(map(int, re.findall(r" (\d+) red", s)))),
                sum(list(map(int, re.findall(r"(\d+) blue", s)))),
                sum(list(map(int, re.findall(r"(\d+) green", s)))),
            ]
            if not (
                games[i][0] <= bag["red"]
                and games[i][1] <= bag["blue"]
                and games[i][2] <= bag["green"]
            ):
                break

            # print(games[i])
        if (
            games[i][0] <= bag["red"]
            and games[i][1] <= bag["blue"]
            and games[i][2] <= bag["green"]
        ):
            ids.append(i + 1)
            valid += i + 1

    #print(games)
    #print(ids)
    return valid

def p2(inp):
    rgb = 0
    games = [[0, 0, 0] for i in range(len(inp))]
    
    for i in range(len(inp)):
        sets = inp[i]
        #print(sets)
        for s in sets:
            # print(s)
            games[i] = [
                max(games[i][0], sum(list(map(int, re.findall(r" (\d+) red", s))))),
                max(games[i][1],sum(list(map(int, re.findall(r"(\d+) blue", s))))),
                max(games[i][2],sum(list(map(int, re.findall(r"(\d+) green", s)))))
            ]
        rgb += games[i][0] * games[i][1] * games[i][2]

    return rgb
    
    

def process_input():
    inp = open(0, encoding="utf-8 ").read().splitlines()
    inp = [l.strip().split(";") for l in inp]

    return f"Part 1: {p1(inp)}\tPart 2: {p2(inp)}"

    # code


if __name__ == "__main__":
    # Read input

    # Process and output result
    print("Solution:", process_input())
