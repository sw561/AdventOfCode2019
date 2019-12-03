#!/usr/bin/env python3

from collections import defaultdict

def distance(d, pos, x, y):
    return d + abs(pos[0] - x) + abs(pos[1] - y)

HORIZONTAL = 0
VERTICAL = 1

def segments(steps):
    # Generate a sequence of line segments
    pos = (0, 0)
    distance = 0
    for step in steps:
        direction, length = step[0], int(step[1:])
        if direction == 'R':
            new_pos = (pos[0] + length, pos[1])
            segment = HORIZONTAL, pos[1], (pos[0], new_pos[0]), distance, pos
        elif direction == 'L':
            new_pos = (pos[0] - length, pos[1])
            segment = HORIZONTAL, pos[1], (new_pos[0], pos[0]), distance, pos
        elif direction == 'U':
            new_pos = (pos[0], pos[1] + length)
            segment = VERTICAL, pos[0], (pos[1], new_pos[1]), distance, pos
        elif direction == 'D':
            new_pos = (pos[0], pos[1] - length)
            segment = VERTICAL, pos[0], (new_pos[1], pos[1]), distance, pos

        yield segment
        pos = new_pos
        distance += length

def segment_database(it):
    # it is an iterator which returns segments
    database = defaultdict(list)
    for d, fixed, seg, distance, pos in it:
        database[(d, fixed)].append((seg, distance, pos))

    return database

def intersections(database, segment):
    d, fixed, (start, end), d1, p1 = segment

    for iter_index in range(start, end+1):
        # Get database segments in opposite orientation
        for (s, e), d2, p2 in database[(1-d, iter_index)]:
            if s <= fixed <= e:
                if d is HORIZONTAL:
                    x, y = iter_index, fixed
                else:
                    x, y = fixed, iter_index
                yield ((x, y),
                    distance(d1, p1, x, y),
                    distance(d2, p2, x, y))

def solve(a, b):
    database = segment_database(segments(a))

    min_manhattan = None
    min_delay = None
    for segment in segments(b):
        for intersection, d1, d2 in intersections(database, segment):
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
