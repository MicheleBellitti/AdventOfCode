rps_scores = {'R': 1, 'P': 2, 'S': 3}
enemy_map = {'A': 'R', 'B': 'P', 'C': 'S'}
player_map = {'X': 'R', 'Y': 'P', 'Z': 'S'}
confr = {'RP': 6, 'PS': 6, 'SR': 6, 'PR': 0, 'SP': 0, 'RS': 0, 'RR': 3, 'PP': 3, 'SS': 3}
win = {'R': 'P', 'P': 'S', 'S': 'R'}
loose = {'R': 'S', 'P': 'R', 'S': 'P'}


def part2(a, b):

    if b == 'X':
        return 0 + rps_scores[loose[a]]
    if b == 'Y':
        return 3 + rps_scores[a]
    if b == 'Z':
        return 6 + rps_scores[win[a]]


score_1 = 0
score_2 = 0
plays = [line.strip() for line in open('input#2.txt', 'r').readlines()]
for p in plays:
    a, b = p.split()
    a = enemy_map[a]
    score_2 += part2(a, b)
    b = player_map[b]
    score_1 += confr[a + b] + rps_scores[b]

print(f'part 1: {score_1}\t|\tpart 2: {score_2}')
