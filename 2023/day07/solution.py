from datetime import datetime

from aocd import get_data, submit

letter_map = {'T':'A', 'J':'.', 'Q':'C', 'K':'D', 'A':'E'} # use "J": "B" for part #1 
def get_rank(hand):
    counts = [hand.count(c) for c in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        return 4 if 2 in counts else 3
    if 2 in counts:
        return 2 if counts.count(2) == 4 else 1
    return 0
def sort_hands(hand, func):
    return (func(hand), [letter_map.get(c, c) for c in hand])
def p1(inp):
    
    plays = []
    for line in inp:

        hand, bind = line.strip().split()
        plays.append((hand, int(bind)))
    plays.sort(key=lambda x: sort_hands(x[0], get_rank))



    return sum((i+1)*plays[i][1] for i in range(len(plays)))

def replacements(hand):
    if hand == "": 
        return [""]
    else:
        return [
        x+y
        for x in ('23456789TQKA' if hand[0] == 'J' else hand[0])
        for y in replacements(hand[1:])
    ]
def classify_with_joker(hand):
    return max(map(get_rank, replacements(hand)))

def p2(inp):
    
    plays = []
    for line in inp:

        hand, bind = line.split()
        plays.append((hand, int(bind)))

    plays.sort(key=lambda x: sort_hands(x[0], classify_with_joker))
    # print(plays)
    return sum((i+1)*plays[i][1] for i in range(len(plays)))

def process_input(year, day):
    inp = open(0, encoding='utf-8').readlines()
    # inp = get_data(day=day, year=year)
    print(inp)
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    #submit(p_2, part='b', day=day, year=year)
    return p_1, p_2

if __name__ == "__main__":
    y = datetime.now().year
    d = 7
    
    # Process and output result
    print("Solution:", process_input(y, d))
