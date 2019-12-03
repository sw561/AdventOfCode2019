#!/usr/bin/env python3

from collections import defaultdict

class DistanceFunc:
    def __init__(self, distance, ref):
        self.distance = distance
        self.ref = ref

class HorizontalDist(DistanceFunc):
    def __call__(self, x, y):
        return self.distance + abs(x - self.ref)

class VerticalDist(DistanceFunc):
    def __call__(self, x, y):
        return self.distance + abs(y - self.ref)

def segments(steps):
    # Generate a sequence of line segments
    pos = (0, 0)
    distance = 0
    for step in steps:
        direction, length = step[0], int(step[1:])
        if direction == 'R':
            new_pos = (pos[0] + length, pos[1])
            segment = 'H', pos[1], (pos[0], new_pos[0]), HorizontalDist(distance, pos[0])
        elif direction == 'L':
            new_pos = (pos[0] - length, pos[1])
            segment = 'H', pos[1], (new_pos[0], pos[0]), HorizontalDist(distance, pos[0]) 
        elif direction == 'U':
            new_pos = (pos[0], pos[1] + length)
            segment = 'V', pos[0], (pos[1], new_pos[1]), VerticalDist(distance, pos[1])
        elif direction == 'D':
            new_pos = (pos[0], pos[1] - length)
            segment = 'V', pos[0], (new_pos[1], pos[1]), VerticalDist(distance, pos[1])

        yield segment
        pos = new_pos
        distance += length

def segment_database(it):
    # it is an iterator which returns segments
    horizontal = defaultdict(list)
    vertical = defaultdict(list)
    for d, fixed, seg, distance_func in it:
        if d == 'H':
            horizontal[fixed].append((seg, distance_func))
        else: # d == 'V'
            vertical[fixed].append((seg, distance_func))

    return horizontal, vertical

def intersections(horizontal, vertical, segment):
    d, fixed, (start, end), distance_func = segment
    if d == 'H':
        # horizontal, check for intersections with database for vertical segments
        for x in range(start, end+1):
            for (s, e), d_func in vertical[x]:
                if s <= fixed <= e:
                    yield (x, fixed), distance_func(x, fixed), d_func(x, fixed)

    else: # d == 'V'
        # vertical, check for intersections with database for horizontal segments
        for y in range(start, end+1):
            for (s, e), d_func in horizontal[y]:
                if s <= fixed <= e:
                    yield (fixed, y), distance_func(fixed, y), d_func(fixed, y)


def solve(a, b):
    h, v = segment_database(segments(a))

    min_manhattan = None
    min_delay = None
    for segment in segments(b):
        for intersection, d1, d2 in intersections(h, v, segment):
            manhattan = sum(map(abs, intersection))
            delay = d1 + d2

            if manhattan == 0:
                continue

            print(intersection, d1, d2)

            if min_manhattan is None or manhattan < min_manhattan:
                min_manhattan = manhattan

            if min_delay is None or delay < min_delay:
                min_delay = delay

    return min_manhattan, min_delay

if __name__=="__main__":

    with open("03_crossed_wires/input.txt", 'r') as f:
        a, b = (line.split(',') for line in f)

    min_manhattan, min_delay = solve(a, b)
    print(min_manhattan)
    print(min_delay)
