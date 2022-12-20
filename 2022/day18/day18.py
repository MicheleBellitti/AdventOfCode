import matplotlib.pyplot as plt
import numpy as np
import fill_voids

data = []


def get_cube(x, y, z):
    c = []
    for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
        c.append([x + dx, y + dy, z + dz])
    c = [cc for cc in c if cc[0] >= 0 and cc[1] >= 0 and cc[2] >= 0]
    return c


with open('input#18.txt') as f:
    for line in f:
        data.append([*map(int, line.strip().split(','))])

data = np.array(data)
max_x, max_y, max_z = data[:, 0].max(), data[:, 1].max(), data[:, 2].max()

grid = np.zeros((max_x + 1, max_y + 1, max_z + 1))
for pos in data:
    grid[pos[0], pos[1], pos[2]] = 1

filled_image = fill_voids.fill(grid, in_place=False)
data = data.tolist()
x = np.vstack((np.where(filled_image == 1))).T
data_2 = [list(xx) for xx in x]

nei = []
neigh = []
for v in data:
    nei.append(sum([1 for a in get_cube(*v) if a in data]))

for vv in data_2:

    neigh.append(sum([1 for a in get_cube(*vv) if a in data_2]))

part1 = sum([6 - n for n in nei])
part2 = sum([6 - n for n in neigh])
print(f'Part 1: {part1}\t|\tPart 2: {part2}')
