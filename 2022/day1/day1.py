cals = list()
i = 0
with open('input#1.txt', 'r') as f:
    cal = 0
    for _ in range(2254):
        inp = f.readline().strip()

        if inp == '':
            cals.append(cal)
            cal = 0
            i += 1
        else:
            cal += int(inp)

cals.sort(reverse=True)
print(f'part 1: {cals[0]}\t|\tpart 2: {sum(cals[0:3])}')


