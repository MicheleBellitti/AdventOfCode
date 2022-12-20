import copy
import time


def decrypt(nums):
    for i in range(len(nums)):
        i, entry = next((j, entry) for j, entry in enumerate(nums) if entry[0] == i)
        j = (i + entry[1]) % (len(nums) - 1)
        if i < j:
            nums[i:j] = nums[i + 1: j + 1]
        elif i > j:
            nums[j + 1: i + 1] = nums[j:i]
        nums[j] = entry
    return nums


desc_key = 811589153
encrypt = [(pos, int(line)) for pos, line in enumerate(open('input#20.txt').readlines())]
start = time.time()
# part 1 #
encrypt = decrypt(encrypt)

zero_idx = [x[1] for x in encrypt].index(0)

part1 = sum(encrypt[(zero_idx + offset) % len(encrypt)][1] for offset in [1000, 2000, 3000])
time1 = time.time() - start
# part 2 #
encrypt = [(pos, int(line)*desc_key) for pos, line in enumerate(open('input#20.txt').readlines())]

start = time.time()
for _ in range(10):
    encrypt = decrypt(encrypt)

zero_idx = [x[1] for x in encrypt].index(0)
part2 = sum(encrypt[(zero_idx + offset) % len(encrypt)][1] for offset in [1000, 2000, 3000])
time2 = time.time() - start
# print results #
print(f'Part 1: {part1}\t|\tPart 2: {part2}')
print(f'Time of execution: Part 1: {time1:.3f}s\t|\tPart 2: {time2:.3f}s')
