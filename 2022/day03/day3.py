sacks = [line.strip() for line in open('input#3.txt', 'r').readlines()]
prio_1 = {alpha: i + 1 for i, alpha in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower())}
prio_2 = {alpha: 27 + i for i, alpha in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def part1():
    prios_sum1 = 0
    for sack in sacks:
        s1, s2 = set(sack[:len(sack) // 2]), set(sack[len(sack) // 2:])
        intersec = s1 & s2
        for i in intersec:
            if i.islower():
                prios_sum1 += prio_1[i]
            else:
                prios_sum1 += prio_2[i]
    return prios_sum1

def part2():
    prios_sum2 = 0
    for s in range(0,len(sacks),3):
        s1, s2, s3 = sacks[s:s + 3]
        for i in range(len(s1)):
            if s1[i] in s2 and s1[i] in s3 and s1.index(s1[i]) == i:
                if s1[i].islower():
                    prios_sum2 += prio_1[s1[i]]
                else:
                    prios_sum2 += prio_2[s1[i]]
    return prios_sum2

print(f'part 1: {part1()}  |  part 2: {part2()}')