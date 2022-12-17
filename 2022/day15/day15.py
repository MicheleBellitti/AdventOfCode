#!/usr/bin/env python3

import pathlib
import re
import sys
from time import perf_counter
from typing import Tuple, Dict, Set

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))

MapPoint = Tuple[int, int]
SensorMap = Dict[MapPoint, int]
BeaconSet = Set[MapPoint]


class RangeSet():
    def __init__(self) -> None:
        self.ranges = []

    def __contains__(self, n: int) -> bool:
        return any(r[0] <= n <= r[1] for r in self.ranges)

    def add(self, rng) -> None:
        idx = next((i for i, r in enumerate(self.ranges) if not r[1] < rng[0]), len(self.ranges))
        if idx == len(self.ranges):
            self.ranges.append(rng)
        elif self.ranges[idx][0] > rng[1]:
            self.ranges.insert(idx, rng)
        else:
            self.ranges[idx] = (min(self.ranges[idx][0], rng[0]), max(self.ranges[idx][1], rng[1]))
            while idx + 1 < len(self.ranges) and self.ranges[idx + 1][0] <= self.ranges[idx][1]:
                self.ranges[idx] = (self.ranges[idx][0], max(self.ranges[idx][1], self.ranges.pop(idx + 1)[1]))

        return

    def iter(self):
        return (r for r in self.ranges)


def read_sensors(file: pathlib.Path):
    mapping, beacons = {}, set()

    parser = re.compile(r'Sensor at x=([0-9-]+), y=([0-9-]+): closest beacon is at x=([0-9-]+), y=([0-9-]+)')

    with open(file) as f:
        while line := f.readline().rstrip():
            if m := parser.match(line):
                sx, sy, bx, by = (int(d) for d in m.groups())
                mapping[(sx, sy)] = abs(sx - bx) + abs(sy - by)
                beacons.add((bx, by))

    return mapping, beacons


def count_no_beacons(mapping: SensorMap, beacons: BeaconSet, row: int) -> int:
    ranges = RangeSet()

    for (x, y), r in mapping.items():
        if y - r <= row <= y + r:
            x_dist = r - abs(row - y)
            ranges.add((x - x_dist, x + x_dist))

    count = -sum(1 for (x, y) in beacons if y == row and x in ranges)
    count += sum(hi - lo + 1 for lo, hi in ranges.iter())
    return count


def distress_frequency(map: SensorMap, beacons: BeaconSet, bound: int):
    ranges = [RangeSet() for _ in range(bound + 1)]

    for (x, y), r in map.items():
        if y + r < 0 or y - r > bound:
            continue

        for row in range(max(0, y - r), min(bound, y + r) + 1):
            x_dist = r - abs(row - y)
            if x + x_dist < 0 or x - x_dist > bound:
                continue

            ranges[row].add((max(0, x - x_dist), min(bound, x + x_dist)))

    for y in range(bound + 1):
        for x, (lo, hi) in enumerate(ranges[y].iter()):
            if hi != bound:
                return (hi + 1) * 4000000 + y
            elif lo != 0:
                return (lo - 1) * 4000000 + y

    return 0


def run():
    file, row = 'input#15.txt', 2000000
    s_map, beacons = read_sensors(file)

    count = count_no_beacons(s_map, beacons, row)


    frequency = distress_frequency(s_map, beacons, row * 2)
    print(f'Part 1: {count}\t|\tPart 2: {frequency}')


if __name__ == '__main__':
    c = perf_counter()
    run()
    print(f'Elapsed time: {perf_counter() - c:.3f}s')
    sys.exit(0)
