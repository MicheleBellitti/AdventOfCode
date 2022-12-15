
rocks = list()
with open("input#14.txt") as f:
    rocks.extend([list(map(eval, s.strip().split(' -> '))) for s in f.read().splitlines()])
max_y = max([xy[1] for ridge in rocks for xy in ridge])
max_x = max([xy[0] for ridge in rocks for xy in ridge])


def fill_paths():
    for r in rocks:
        for i in range(len(r) - 1):
            x1, y1, x2, y2 = r[i][0], r[i][1], r[i + 1][0], r[i + 1][1]
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cave_floor[y][x] = '#'


def fall() -> bool:
    (x, y) = (500, 0)
    while y < max_y:
        y += 1
        if cave_floor[y][x] == '.':
            continue
        elif cave_floor[y][x - 1] == '.':
            x -= 1
        elif cave_floor[y][x + 1] == '.':
            x += 1
        else:
            cave_floor[y - 1][x] = 'o'
            return True
    return False


# Part 1

cave_floor = [['.'] * (max_x + 2) for _ in range(max_y + 1)]
fill_paths()
grains_1 = 0
while fall():
    grains_1 += 1



# Part 2

max_y += 2
cave_floor = [['.'] * (501 + max_y) for _ in range(max_y)]
cave_floor += [['#'] * (501 + max_y)]
fill_paths()
grains_2 = 0
while cave_floor[0][500] == '.':
    fall()
    grains_2 += 1


print(f'Part 1: {grains_1}\t|\tPart 2: {grains_2}')


