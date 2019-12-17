#!/usr/bin/env python3

from solve import alignment_parameters

def assertEqual(x, y):
    try:
        assert x == y
    except AssertionError:
        print("{} != {}".format(x, y))
        raise

s = """..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^.."""

assertEqual(sum(alignment_parameters(s)), 76)

print("Test passed")
