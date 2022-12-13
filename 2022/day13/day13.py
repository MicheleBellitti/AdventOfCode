from ast import literal_eval
import functools


data = list()
with open("input#13.txt") as f:
    data = [[literal_eval(t[0]), literal_eval(t[1])] for t in [s.split('\n') for s in f.read().split('\n\n')]]


def compare(l_val, r_val)->int:
    '''
    Recursive function to compare two nested iterable structures.
    @param l_val: The left value.
    @param r_val: The right value.
    @return: The result of the comparison.

    '''
    if isinstance(l_val, int) and isinstance(r_val, int):
        if l_val < r_val: return -1
        elif l_val > r_val:
            return 1
        else:
            return 0

    elif isinstance(l_val, int):
        l_val = [l_val]
    elif isinstance(r_val, int):
        r_val = [r_val]

    if not l_val and r_val: return -1
    if l_val and not r_val : return +1
    if not (l_val or r_val): return 0

    comp = compare(l_val[0], r_val[0])

    return comp if comp else compare(l_val[1:], r_val[1:])

####### PART 1 #######

correct_idx = [i for i in range(1, len(data) + 1) if compare(data[i - 1][0], data[i - 1][1]) == -1]
p1 = sum(correct_idx)

####### PART 2 #######

data = [eval(t) for t in open('input#13.txt').read().split()] + [[[2]]] + [[[6]]]
data.sort(key=functools.cmp_to_key(compare))
p2 = (1 + data.index([[2]])) * (1 + data.index([[6]]))

####### OUTPUT #######

print(f"part 1: {p1}\t|\tpart 2: {p2}")
