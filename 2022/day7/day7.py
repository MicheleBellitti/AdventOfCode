f = open('input#7.txt', 'r')
inp = [x.strip().split() for x in f.readlines()]
f.close()

path = {}
sums = {}

curr = []
cnt = 0
for line in inp:
    if line[1] == "cd":
        if line[2] == "..":
            curr.pop()
        else:
            curr.append(line[2])
            path[''.join(curr)] = []
            sums[''.join(curr)] = 0
            cnt = 0
    elif line[1] == "ls":
        continue
    elif line[0] == "dir":
        path["".join(curr)].append("".join(curr) + line[1])
    else:
        sums["".join(curr)] += int(line[0])

total_size = {}
for i in path:
    total_size[i] = 0


def subdir_adj(cnt, i):
    if len(path[i]) > 0:
        for j in path[i]:
            subdir_adj(cnt, j)
    cnt.append(sums[i])


for i in path:
    cnt = []
    subdir_adj(cnt, i)

    total_size[i] += sum(cnt)

result = 0
# part 1
for i in total_size:
    if total_size[i] <= 100000:
        result += total_size[i]
# part 2
used_space = sum(list(sums.values()))
tot_space = 70000000
free_space = 30000000
del_val = tot_space

for i in total_size:
    if (used_space - total_size[i]) <= (tot_space - free_space) and total_size[i] < del_val:
        del_val = total_size[i]

print(f'Part 1: {result}\t|\tPart 1: {del_val}')
