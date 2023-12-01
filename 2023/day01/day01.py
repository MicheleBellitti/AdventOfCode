import re

inp = open('in.txt', encoding='utf-8 ').read().splitlines() # use "test.txt" for small input data
# print(inp)

def filt(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
    x = re.findall(r'(\d)', line)
    
    return int(x[0] + x[-1])

p1 = 0

for v in list(map(lambda x: re.findall(r'\d+', x), inp)):
    p1 += int(f"{v[0][0]}{v[-1][-1]}")
p2 = sum(map(filt, inp))
print(f"Part 1: {p1}\nPart 2: {p2}")