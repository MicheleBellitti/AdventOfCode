
ops = [line.strip().split() for line in open("input#10.txt").readlines()]

register = 1
cycles = 0
sum_1 = 0
sum_2 = 0
crt = [['.' for _ in range(40)] for _ in range(6)]


for op in ops:

    cycles += 1

    if cycles in [20, 60, 100, 140, 180, 220]:
        sum_1 += cycles * register
    if abs((cycles - 1) % 40 - register) < 2:
        crt[(cycles - 1) // 40][(cycles - 1) % 40] = '#'
    if op[0] == 'noop':
        continue
    else:
        for _ in range(1):
            cycles += 1
            if abs((cycles - 1) % 40 - register) < 2:
                crt[(cycles - 1) // 40][(cycles - 1) % 40] = '#'
            if cycles in [20, 60, 100, 140, 180, 220]:
                sum_1 += cycles * register

        register += int(op[1])

# Visualize the CRT
x = open("output#10.txt", "w")

for line in crt:
    x.write(''.join(line))
    x.write('\n')
x.close()

# Results
print(f'part 1: {sum_1}\t|\tpart 2: EALGULPG.')
