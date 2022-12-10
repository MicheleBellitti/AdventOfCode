def bounds(b):
    for index in range(len(b)):
        if b[index] == '-':
            return b[:index], b[index + 1:]


def overlap(b1, b2):
    return (b2[1] >= b1[0] >= b2[0] or b2[1] >= b1[1] >= b2[0]) or (b1[1] >= b2[0] >= b1[0] or b1[1] >= b2[1] >= b1[0])


def contained(b1, b2):
    return (b1[0] >= b2[0] and b1[1] <= b2[1]) or (b1[0] <= b2[0] and b1[1] >= b2[1])


f = open('input#4.txt', 'r')
overlaps = 0
cont = 0
lines = f.readlines()

f.close()
for line in lines:
    line = line.replace('\n', '')
    r1, r2 = line.split(',')
    b1, b2 = tuple(map(int, bounds(r1))), tuple(map(int, bounds(r2)))

    if overlap(b1, b2):
        overlaps += 1
    if contained(b1, b2):
        cont += 1
print(f'part 1: {cont}  |  part 2: {overlaps}')

