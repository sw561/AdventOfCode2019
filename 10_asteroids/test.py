#!/usr/bin/env python3

from solve import get_positions, los_array, part1, part2

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

m = """
.#..#
.....
#####
....#
...##""".split()

positions = get_positions(m)
los = los_array(m, positions)

count, id_max = part1(positions, los)

assertEqual(positions[id_max], (3, 4))
assertEqual(count, 8)

m = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split()


positions = get_positions(m)
los = los_array(m, positions)

count, id_max = part1(positions, los)
assertEqual(positions[id_max], (11, 13))
assertEqual(count, 210)

vap = part2(positions, los, id_max)

for index, pos in [
        (1, (11,12)),
        (2, (12,1)),
        (3, (12,2)),
        (10, (12,8)),
        (20, (16,0)),
        (50, (16,9)),
        (100, (10,16)),
        (199, (9,6)),
        (200, (8,2)),
        (201, (10,9)),
        (299, (11,1)),
        ]:
    assertEqual(positions[vap[index-1]], pos)

print("Test passed")
